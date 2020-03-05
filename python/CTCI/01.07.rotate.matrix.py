# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel
# in the image is 4 bytes, write a method to rotate the image by 90 degrees.
# Can you do this in place? Hints: #51, #100

# Caveat: "WHERE EACH PIXEL IS 4 BYTES", what does this mean??!
# Will assume each element a 4-byte int

# APPROACH:
# Since the challenge is to rotate the matrix in place, we can treat the matrix
# as a series of shells or layers. We would rotate the outermost shell and move
# to the next until finishing the innermost

# Within each shell, we would store the value of the matrix at each point, and
# replace it with the value of the matrix at -90 degrees, following a windmill
# spiral of 4 points

# Example:
#   1  2  3  4  5
#  16  .  .  .  6
#  15  .  .  .  7
#  14  .  .  .  8
#  13 12 11 10  9

# store 1
# replace 1 with 5
# replace 5 with 9
# replace 9 with 13
# replace 13 with stored 1

# store 2
# replace 2 with 6
# replace 6 with 10
# replace 10 with 14
# replace 14 with stored 2

# continue until row - 1 has been rotated
# move to next inner shell if possible

# The number of layers of a n x n matrix = floor(n / 2) + n % 2
