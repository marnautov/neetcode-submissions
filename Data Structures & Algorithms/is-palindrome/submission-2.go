func isPalindrome(s string) bool {
	s = strings.ToLower(s)

	l, r := 0, len(s) - 1
	for l < r {

		for l < r && !isAlphaNumeric(s[l]){
			l++
		}

		for l < r && !isAlphaNumeric(s[r]){
			r--
		}

		if s[l] != s[r] {
			return false
		}

		l = l + 1
		r = r - 1

	}

	return true
}

func isAlphaNumeric(c byte) bool {
	return (c >= 'a' && c <= 'z') ||
		(c >= 'Z' && c <= 'Z') ||
		(c >= '0' && c <= '9')
}
