#shellshock fix. Nuke the whole feature from orbit, it's the only way to be sure. -@andreasdotorg

diff --git a/variables.c b/variables.c
index cdc54bc..1a98efa 100644
--- a/variables.c
+++ b/variables.c
@@ -347,85 +347,25 @@ initialize_shell_variables (env, privmode)
 
       temp_var = (SHELL_VAR *)NULL;
 
-      /* If exported function, define it now.  Don't import functions from
-	 the environment in privileged mode. */
-      if (privmode == 0 && read_but_dont_execute == 0 && STREQN ("() {", string, 4))
+      ro = 0;
+      if (posixly_correct && STREQ (name, "SHELLOPTS"))
 	{
-	  string_length = strlen (string);
-	  temp_string = (char *)xmalloc (3 + string_length + char_index);
-
-	  strcpy (temp_string, name);
-	  temp_string[char_index] = ' ';
-	  strcpy (temp_string + char_index + 1, string);
-
-	  if (posixly_correct == 0 || legal_identifier (name))
-	    parse_and_execute (temp_string, name, SEVAL_NONINT|SEVAL_NOHIST);
-
-	  /* Ancient backwards compatibility.  Old versions of bash exported
-	     functions like name()=() {...} */
-	  if (name[char_index - 1] == ')' && name[char_index - 2] == '(')
-	    name[char_index - 2] = '\0';
-
-	  if (temp_var = find_function (name))
-	    {
-	      VSETATTR (temp_var, (att_exported|att_imported));
-	      array_needs_making = 1;
-	    }
-	  else
-	    {
-	      if (temp_var = bind_variable (name, string, 0))
-		{
-		  VSETATTR (temp_var, (att_exported | att_imported | att_invisible));
-		  array_needs_making = 1;
-		}
-	      last_command_exit_value = 1;
-	      report_error (_("error importing function definition for `%s'"), name);
-	    }
-
-	  /* ( */
-	  if (name[char_index - 1] == ')' && name[char_index - 2] == '\0')
-	    name[char_index - 2] = '(';		/* ) */
+	  temp_var = find_variable ("SHELLOPTS");
+	  ro = temp_var && readonly_p (temp_var);
+	  if (temp_var)
+	    VUNSETATTR (temp_var, att_readonly);
 	}
-#if defined (ARRAY_VARS)
-#  if ARRAY_EXPORT
-      /* Array variables may not yet be exported. */
-      else if (*string == '(' && string[1] == '[' && string[strlen (string) - 1] == ')')
+      temp_var = bind_variable (name, string, 0);
+      if (temp_var)
 	{
-	  string_length = 1;
-	  temp_string = extract_array_assignment_list (string, &string_length);
-	  temp_var = assign_array_from_string (name, temp_string);
-	  FREE (temp_string);
-	  VSETATTR (temp_var, (att_exported | att_imported));
+	  if (legal_identifier (name))
+	    VSETATTR (temp_var, (att_exported | att_imported));
+	  else
+	    VSETATTR (temp_var, (att_exported | att_imported | att_invisible));
+	  if (ro)
+	    VSETATTR (temp_var, att_readonly);
 	  array_needs_making = 1;
 	}
-#  endif /* ARRAY_EXPORT */
-#endif
-#if 0
-      else if (legal_identifier (name))
-#else
-      else
-#endif
-	{
-	  ro = 0;
-	  if (posixly_correct && STREQ (name, "SHELLOPTS"))
-	    {
-	      temp_var = find_variable ("SHELLOPTS");
-	      ro = temp_var && readonly_p (temp_var);
-	      if (temp_var)
-		VUNSETATTR (temp_var, att_readonly);
-	    }
-	  temp_var = bind_variable (name, string, 0);
-	  if (temp_var)
-	    {
-	      if (legal_identifier (name))
-		VSETATTR (temp_var, (att_exported | att_imported));
-	      else
-		VSETATTR (temp_var, (att_exported | att_imported | att_invisible));
-	      if (ro)
-		VSETATTR (temp_var, att_readonly);
-	      array_needs_making = 1;
-	    }
-	}
 
       name[char_index] = '=';
       /* temp_var can be NULL if it was an exported function with a syntax