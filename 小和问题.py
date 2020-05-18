def get_smallSum(arr):
    if arr is None or len(arr) < 2:
        return 0
    return ssSum(arr, 0, len(arr) - 1)
def ssSum(arr, l, r):
    if l == r:
        return 0
    mid = l +( (r - l) // 2)
    return ssSum(arr, l, mid) + ssSum(arr, mid + 1, r) + merge(arr, l, mid, r)
# 求左半部分的小和 + 右半部分的小和 + 合并产生的小和
def merge(arr,l,mid,r):
    left = l
    right = mid + 1
    res = []
    sum = 0
    # 在归并排序中求得小和
    while left<=mid and right<=r:
        # 只有右边大于左边才会贡献小和
        if arr[left] < arr[right]:
            sum += arr[left]*(r-right+1)
            res.append(arr[left])
            left+=1
        else:
            res.append(arr[right])
            right+=1
    while left<=mid:
        res.append(arr[left])
        l+=1
    while right<=r:
        res.append(arr[right])
        right+=1
    arr[l:r+1] = res
    return sum
if __name__ == "__main__":
    arr = [1, 3, 4, 2, 5]
    print(get_smallSum(arr))