func containsNearbyDuplicate(nums []int, k int) bool {
	seen := make(map[int]int)

	for i, num := range nums {
		if prev, ok := seen[num]; ok && i-prev <= k {
			return true
		}
		seen[num] = i
	}
	return false
}
