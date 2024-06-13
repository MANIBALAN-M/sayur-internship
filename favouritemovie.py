'''
############## Problem  1 #################### 
#Ask first friend the movies they like. Save it in a list
#Ask another friend the same question. If the movie is in the first friend's list, 
#Print "You both like "name of the movie"
#Continue until they is atleast 3 movies they both like

#init variables
movies = input("What movies you like ? ):
#convert movies into a List
#FillinMissingCode

commonMoviewCount = 0
while (True) :
    #ask the second friend for one movie at a time
    movie = input ( )#FillinMissingCode)
    #Check if this movie is in the movie list
    #FillinMissingCode

    #if present, 
    commonMoviewCount ++
    #check if we reached the max
    if(commmonMovieCount >= 3):
        break;
    else
        print ("Try again")

print () #FillinMissingCode - list all the common movies

'''
import sys
condition=1
count=0
while condition == 1:
    num_of_movie1 = int(input('enter number of movies: '))
    fav_movie1_list =[]
    for i in range(num_of_movie1):
        fav_movie1 = input(f'enter favourite movies of person 1 movie number {i+1}: ')
        fav_movie1_list.append(fav_movie1)
    print(fav_movie1_list)
    num_of_movie2 = int(input('enter number of movies: '))
    fav_movie2_list =[]
    for j in range(num_of_movie2):
        fav_movie2 = input(f'enter favourite movies of person 2 movie number {j+1}: ')
        fav_movie2_list.append(fav_movie2)
    print(fav_movie2_list)
    for i in range(len(fav_movie1_list)):
        for j in range(len(fav_movie2_list)):
            if fav_movie1_list[i]==fav_movie2_list[j]:
                count=count+1
    if count>=3:
        print('you and your friend like same movies')
        condition=0
                    
    

      
      
      
      
'''


for i in range(len(fav_movie1_list)):
        if fav_movie1_list[i]==fav_movie2_list[i]:
            count=count +1
        if count==3:
            print('you and your friend like same movbies')
            condition=0



'''




        
