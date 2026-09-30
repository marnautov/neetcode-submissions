import "slices"

func heightChecker(heights []int) int {
	
	sortedHeights := slices.Clone(heights)
	slices.Sort(sortedHeights)

	count := 0
	for i := range heights {
		if heights[i] != sortedHeights[i] {
			count++
		}
	}

	return count
}