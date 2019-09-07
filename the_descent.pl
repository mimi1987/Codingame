use strict;
use warnings;
#use diagnostics;
use 5.20.1;

select(STDOUT); $| = 1; # DO NOT REMOVE

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.


# game loop
while (1) {
    my $max = 0;
    my $imax = 0;
    for my $i (0..7) {
        chomp(my $mountain_h = <STDIN>); # represents the height of one mountain.
        if ($max < $mountain_h) {
            $max = $mountain_h;
            $imax = $i;
        }
    }
    
    # Write an action using print
    # To debug: print STDERR "Debug messages...\n";

    print "$imax\n"; # The index of the mountain to fire on.
}
