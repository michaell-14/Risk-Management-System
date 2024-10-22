# Set to C++ 20 and add error flags
CPPFLAGS := -std=gnu++20 -pedantic-errors -Wall -Wextra -Werror 
COMPILER := g++

# Name the executable
TARGET := monteTest

# Find all .cpp files and corresponding .o files
SRCS := $(wildcard *.cpp) # Find all .cpp files; wildcard is a function that finds all files with a certain folder
OBJS := $(SRCS:.cpp=.o) # Replace .cpp with .o; object files are the compiled files

# Build the executable
$(TARGET): $(OBJS)
    $(COMPILER) -o $(TARGET) $(OBJS)

# Compile .o files from .cpp files
%.o: %.cpp
    $(COMPILER) -c $(CPPFLAGS) $< -o $@

# Clean up the directory
clean:
    rm -f *.o $(TARGET)

# Make and run the program in one command
run: # Name of the target; run is the name of the target
    make clean
    make 
    ./$(TARGET)

