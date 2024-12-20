package main

import "fmt"

func main() {
	nums1 := []int{2, 7, 11, 15}
	nums2 := []int{3, 2, 4}
	nums3 := []int{3, 3}

	target1 := 9
	target2 := 6
	target3 := 6

	a := twoSum(nums1, target1)
	b := twoSum(nums2, target2)
	c := twoSum(nums3, target3)

	fmt.Println(a)
	fmt.Println(b)
	fmt.Println(c)
}

//used knowledge from my Python solution to complete
func twoSum(nums []int, target int) []int {
    for i := 0; i < len(nums); i++ {
        for j := i+1; j < len(nums); j++ {
            if nums[j] == target - nums[i] {
                return []int{i, j}
            }   
        }
    }
    return []int{}
}

//Ex2 from LeetCode
/*
func twoSum(nums []int, target int) []int {
    m := make(map[int]int)
    for i, num := range nums {
        m[num] = i
    }
    for i, num := range nums {
        complement := target - num
        if j, ok := m[complement]; ok && j != i {
            return []int{i, j}
        }
    }
    // Return an empty slice if no solution is found
    return []int{}
}
*/

//Ex3 from LeetCode
/*
func twoSum(nums []int, target int) []int {
    m := make(map[int]int)
    for i, num := range nums {
        complement := target - num
        if j, ok := m[complement]; ok {
            return []int{j, i}
        }
        m[num] = i
    }
    // Return an empty slice if no solution is found
    return []int{}
}
*/


