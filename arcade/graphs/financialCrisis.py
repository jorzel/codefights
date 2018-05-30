"""
Once upon a time, in a kingdom far, far away, there lived a king Byteasar IV. As Interkingdomial financial crisis was roaring through the neighborhood, Byteasar was struggling with keeping the economy out of recession. Unfortunately there was not much he could do. After long and deep thinking, the king came to the only solution: one of his cities should be demolished, since keeping communication between all the cities is way too expensive.

It is not yet known if Byteasar chose the city to destroy after a careful planning or picked one at random. As a person with PhD in history and Nobel prize in Computer Science, you can solve this mystery. Archaeologists have recently found a manuscript with the information about the roads between the cities, that is now stored in the roadRegister matrix. You want to try and remove each city one by one and compare the road registers obtained this way. Thus you'll be able to compare the obtained roads and determine whether the one picked by Byteasar was the best by some criteria.

Given the roadRegister, return an array of all the road registers obtained after removing each of the city one by one.

Example

For

roadRegister = [[false, true,  true,  false],
                [true,  false, true,  false],
                [true,  true,  false, true ],
                [false, false, true,  false]]
the output should be

financialCrisis(roadRegister) = [
  [[false, true,  false],
   [true,  false, true ],
   [false, true,  false]],
  [[false, true,  false],
   [true,  false, true ],
   [false, true,  false]],
  [[false, true,  false],
   [true,  false, false],
   [false, false, false]],
  [[false, true,  true ],
   [true,  false, true ],
   [true,  true,  false]]
]
Here's the city connection that the given catalog represents:


And here's how the cities are connected with one of the cities destroyed (cities 0 - 3, respectively):
"""

def financialCrisis(roads):
    _size = len(roads)
    return [[[roads[row][col] for col in range(_size) if col != city] for row in range(_size) if row != city] for city in range(_size)]

    
