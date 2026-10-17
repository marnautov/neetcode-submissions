// import "strconv"

func calPoints(operations []string) int {
	stack := []int{}

	for i := 0; i < len(operations); i++ {
		if operations[i] == "+" {
			stack = append(stack, stack[len(stack) - 1] + stack[len(stack) - 2])
		} else if operations[i] == "D" {
			stack = append(stack, stack[len(stack) - 1] * 2)
		} else if operations[i] == "C" {
			stack = stack[:len(stack) - 1]
		} else {
			num, _ := strconv.Atoi(operations[i])
			stack = append(stack, num)
		}
	}

	sum := 0
	for _, v := range(stack) {
		sum += v
	}

	return sum
}
