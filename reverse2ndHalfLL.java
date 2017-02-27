private static ListNode reverse2(ListNode head) {
		if (head == null || head.next == null) {
			return head;
		}
		ListNode slow = head, fast = head.next;
		while (fast.next != null && fast.next.next != null) {
			slow = slow.next;
			fast = fast.next.next;
		}
		ListNode pre = null;
		ListNode curr = slow.next;
		while (curr != null) {
			ListNode temp = curr.next;
			curr.next = pre;
			pre = curr;
			curr = temp;
		}
		slow.next = pre;
		return head;
	}
