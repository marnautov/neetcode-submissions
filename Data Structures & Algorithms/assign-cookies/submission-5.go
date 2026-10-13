import (
	"slices"
)

func findContentChildren(g []int, s []int) int {
	slices.Sort(g)
	slices.Sort(s)

	j := 0
	for i := 0; i < len(s) && j < len(g); i++ {
		if s[i] >= g[j] {
			j++
		}
	}

	return j
}
