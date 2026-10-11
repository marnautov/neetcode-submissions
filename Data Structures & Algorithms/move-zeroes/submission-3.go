func moveZeroes(nums []int) {
	l := 0

	for r := 0; r < len(nums); r++ {
		if nums[r] != 0 {
			nums[r], nums[l] = nums[l], nums[r]
			l++
		}
	}
}
