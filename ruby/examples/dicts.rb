#!/usr/bin/env ruby

if __FILE__ == $0
    my_dict = {}
    my_dict[:a] = "Symbol"
    my_dict["a"] = "String"
    my_dict[1] = "Integer"
    puts my_dict.keys
    puts my_dict.values
    # What will be deleted?
    my_dict.delete 1
    puts my_dict
end
