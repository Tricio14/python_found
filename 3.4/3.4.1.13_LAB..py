# step 1
beatles_list = []
print("Step 1:", beatles_list)

# step 2
beatles_list.append("John Lennon")
beatles_list.append("Paul McCartney")
beatles_list.append("George Harrison")
print("Step 2:", beatles_list)

# step 3
for members in range(2):
    beatles_list.append(input("New band member: "))
print("Step 3:", beatles_list)

# step 4
del beatles_list[-1]
del beatles_list[-1]
print("Step 4:", beatles_list)

# step 5
beatles_list.insert(0, "Ringo Starr")
print("Step 5:", beatles_list)


# testing list legth
print("The Fab", len(beatles_list))