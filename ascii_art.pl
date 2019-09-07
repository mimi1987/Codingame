use strict;
use warnings;
#use diagnostics;
use 5.20.1;

select(STDOUT); $| = 1; # DO NOT REMOVE

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

chomp(my $l = <STDIN>);
chomp(my $h = <STDIN>);
chomp(my $t = <STDIN>);

$t = uc $t;
my $alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ?";

my @rows = ();

for my $i (0..$h-1) {
    chomp(my $row = <STDIN>);
    push @rows, $row;
}

for my $row (@rows) {
    for my $c (split //, $t) {
        if (index($alphabet, $c) != -1) {
            print(substr($row, index($alphabet,$c)*$l, $l));
        } else {
            my $length = length($alphabet)-1;
            print(substr($row, $l*$length, $l));
        }
    }
    print "\n";
}

# Write an action using print
# To debug: print STDERR "Debug messages...\n";
