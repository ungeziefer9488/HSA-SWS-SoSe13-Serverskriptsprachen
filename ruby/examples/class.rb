#!/usr/bin/env ruby

class Zombie
    # Constructor
    def initialize( hitpoints = 10 )
        @hitpoints = hitpoints
    end

    def eat_brain( target )
        puts "Mmmhh! Delicious Brain of #{target}."
    end
    private :eat_brain
    def +( other_zombie )
        puts "Super Zombie!"
    end
end

if __FILE__ == $0
    z1 = Zombie.new(3)
    z2 = Zombie.new(42)
    z1 + z2
end
