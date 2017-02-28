#1
def  GigawattPower(batteryOne, batteryTwo, gigawattTarget):
    target_minus = set()
    for c in batteryOne:
        target_minus.add(gigawattTarget-c)
    for c in batteryTwo:
        if c in target_minus:
            return True
    return False


#2
def  improbabilityCalculator(coordinates, remove):
    if remove >= len(coordinates):
        return "0"
    if remove == 0:
        return coordinates
    
    res = ""
    return recurr(coordinates, len(coordinates) - remove, res)
    
def recurr(coordinates, need, res):
    if need <= 0:
        return res
    
    smallest = '9'
    k = 0
    for i in range( len(coordinates) - need + 1):
        if coordinates[i] < smallest:
            smallest = coordinates[i]
            k = i
    return recurr(coordinates[k+1:], need - 1, res + coordinates[k])
        


#3
def  numberOfGroups(venue):
    cnt = 0
    for i in range( len(venue) ):
        for j in range( len(venue[0])):
            if venue[i][j] == 1:
                cnt += 1
                venue[i][j] = -1
                dfs(venue, i,j)
    return cnt

def  dfs(venue, i,j):
    for p in (i-1, i , i+1):
        for q in (j-1, j, j+1):
            if p==i and q == j: continue
            if p< 0 or p >= len(venue): continue
            if q< 0 or q >= len(venue[0]):continue
                
            if venue[p][q] == 1:
                venue[p][q] = -1
                dfs(venue, p, q)
    


#4 
def  reverseButPreserveWhitespace(reverseMe):
    res = ""
    
    i = 0
    while i < len(reverseMe):
        if reverseMe[i] == ' ':
            res += ' '
            i+=1
        else:
            k = i
            while k < len(reverseMe):
                if reverseMe[k] != ' ':
                    k += 1
                else:
                    break
            res += reverseMe[i:k][::-1]
            i = k 
    return res



#5
def  foundInBermudatriangle(x1, y1, x2, y2, x3, y3, px, py, bx, by):
    area = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    if area == 0:
        return 0
   
    p_in = is_in(x1, y1, x2, y2, x3, y3, px, py)
    b_in = is_in(x1, y1, x2, y2, x3, y3, bx, by)
    
    if p_in and not b_in: return 1
    if not p_in and b_in: return 2
    if p_in and b_in: return 3
    if not p_in and not b_in: return 4
    

def  same_side(x1, y1, x2,y2,x3,y3, x4,y4):
    # test whether pt3, and pt4 are on the same side of line pt1->pt2
    k1 = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    k2 = (x2 - x1) * (y4 - y1) - (y2 - y1) * (x4 - x1)
    return k1 * k2 >= 0

def  is_in(x1,y1, x2,y2, x3,y3, x4, y4):
    # test if pt4 is in triangle
    ok1 = same_side( x1,y1, x2,y2, x3,y3, x4, y4 )
    ok2 = same_side( x2,y2, x3,y3, x1,y1, x4, y4 )
    ok3 = same_side( x3,y3, x1,y1, x2,y2, x4, y4 )
    
    return ok1 and ok2 and ok3