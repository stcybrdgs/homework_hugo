def add( x, y ):
    return x + y

def mult( x, y ):
    return x * y


#print(add('1',3))
#print( add('7','3') )
#print( mult('3',3) )

#print( 3 * '3' )  # 333 <-- a stringy operation
#print( '3' * 3 )  # 333 <-- a stringy operation
#print( 3 * 3 )    # 9   <-- an arithmetic operation
#print( '3' * '3') # TypeError !

#print( mult( [4], 3 ) )
#print( mult( [3], 4 ) )

# a = ("John", "Charles", "Mike")
# b = ("Jenny")
# c = ("Jenny", "Christy", "Monica")

# ===================================
# a = [1,2,3]
# b = (1,)
# x = zip(a, b)
# print(tuple(x))
# print( [i*i for i in range(10)] )
# print( [ a_i + b_i for a_i, b_i in zip(a,b) ] )
# ===================================

xx  = [1, 2, [3]]

x = [1, 2, [3,4]]
y  = [4, 5, [6,7]]

print( [ (x_i + y_i) for x_i, y_i in zip(x, y) ] )
print([3] + [6])
