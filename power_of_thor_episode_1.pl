use strict;
use warnings;
#use diagnostics;
use 5.20.1;

select(STDOUT); $| = 1; # DO NOT REMOVE

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

my $tokens;

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
chomp($tokens=<STDIN>);
my ($light_x, $light_y, $initial_tx, $initial_ty) = split(/ /,$tokens);

my $thor_x = $initial_tx;
my $thor_y = $initial_ty;


# game loop
while (1) {
    chomp(my $remaining_turns = <STDIN>); # The remaining amount of turns Thor can move. Do not remove this line.
   
    my $direction_y = "";
    my $direction_x = "";
    # Write an action using print
    # To debug: print STDERR "Debug messages...\n";

    # A single line providing the move to be made: N NE E SE S SW W or NW

    if ($thor_y > $light_y) {
        $direction_y = "N";
        $thor_y -= 1;
    } elsif ($thor_y < $light_y) {
        $direction_y = "S";
        $thor_y += 1;
    }
    
    if ($thor_x > $light_x) {
        $direction_x = "W";
        $thor_x -= 1;
    } elsif ($thor_x < $light_x) {
        $direction_x = "E";
        $thor_x += 1;
    }
    
    print $direction_y . $direction_x . "\n";
}
