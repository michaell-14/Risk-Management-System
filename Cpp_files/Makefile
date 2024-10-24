# Set to C++ 20 and add error flags
CPPFLAGS := -std=gnu++20 -pedantic-errors -Wall -Wextra -Werror
COMPILER := g++

# Name the executable
TARGET := monteTest

# Find all .cpp files and corresponding .o files
SRCS := $(wildcard *.cpp)
OBJS := $(SRCS:.cpp=.o)

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
run: clean $(TARGET)
	./$(TARGET)
