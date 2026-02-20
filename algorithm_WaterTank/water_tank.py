def water_trapped(height):
    left = 0
    right = len(height) - 1

    left_max = 0
    right_max = 0
    water = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1

    return water


arr = [0,4,0,0,0,6,0,6,4,0]
print("Water stored:", water_trapped(arr))
