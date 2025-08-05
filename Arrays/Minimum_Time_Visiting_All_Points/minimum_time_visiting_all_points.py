"""

Minimum time visiting all points

Description: On a 2D plane there are n points with integer coordinates points[i] = [xi, yi]. Return the minimum time in seconds to visit all the points in orer give by points. Moves have these rules: in 1 second you can either move vertically by a unit, horizontally by a unit, or diagonally sqrt(2) units so vertically and horizontally in 1 second, you have to visit the points in the same order as in the array, you are allowed to pass through points that appear later but won't count as a visit

Constraints: points.length == n, 1 <= n <= 100, points[i].length == 2, -1000 <= points[i][0], points[i][1] <= 1000

"""

"""

Approaches: 

Greedy approach would be to go diagonally as much as possible since it will be most advantageous to cover as much distance as possible at each step

Because we have to go in order of the points in the array and start at a given point, there is not much freedom to get a faster path, so it's all about doing diagonals as much as possible

Make as many diagonals as possible until the vertical or horizontal is aligned and do until actually at the point do vertical or horizontal movements and keep doing that on loop until at the end.

find the difference between point 1 and 2 in the x and y direction and the smallest difference to align the points will be the time of the diagonal movements then the remaining vertial or horizontal difference is the remaining time to get to that point

"""

"""

OLD APPROACH: It did not work on very large test cases, so I went back to square one and because we can move diagonally the minimum time is the largest difference in either dimension, so it is simply the max of the differences

def minimum_time(points):
    total_time = 0

    for i in range(len(points) - 1):
        diag_time = 0

        if ((points[i+1][0] - points[i][0]) and (points[i+1][1] - points[i][1])):
            diag_time = min(points[i+1][0] - points[i][0], points[i+1][1] - points[i][1])

        x_diag = diag_time + points[i][0]
        y_diag = diag_time + points[i][1]
        hv_time = (points[i+1][0] - x_diag) + (points[i+1][1] - y_diag) # one of the parenthesis will be zero so don't need extra logic to figure out if it is zero in horizontal or vertical direction

        total_time = total_time + abs(diag_time) + abs(hv_time)
    
    return total_time

"""
def minimum_time(points):
    total_time = 0

    for i in range(len(points) - 1):
        total_time += max(abs(points[i+1][0] - points[i][0]), abs(points[i+1][1] - points[i][1]))
    return total_time

def main():
    points = [[559,511],[932,618],[-623,-443],[431,91],[838,-127],[773,-917],[-500,-910],[830,-417],[-870,73],[-864,-600],[450,535],[-479,-370],[856,573],[-549,369],[529,-462],[-839,-856],[-515,-447],[652,197],[-83,345],[-69,423],[310,-737],[78,-201],[443,958],[-311,988],[-477,30],[-376,-153],[-272,451],[322,-125],[-114,-214],[495,33],[371,-533],[-393,-224],[-405,-633],[-693,297],[504,210],[-427,-231],[315,27],[991,322],[811,-746],[252,373],[-737,-867],[-137,130],[507,380],[100,-638],[-296,700],[341,671],[-944,982],[937,-440],[40,-929],[-334,60],[-722,-92],[-35,-852],[25,-495],[185,671],[149,-452]]
    print(minimum_time(points))

if __name__ == "__main__":
    main()