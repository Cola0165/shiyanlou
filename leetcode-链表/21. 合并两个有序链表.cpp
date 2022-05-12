#include "iostream"

using namespace std;

#include "algorithm"
#include "vector"
#include "queue"
#include "set"
#include "map"
#include "cstring"
#include "stack"

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

struct ListNode {
    int val;
    ListNode *next;

    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
private:
    // 定义新链表的头结点
    ListNode *headNode = NULL;
public:
    ListNode *mergeTwoLists(ListNode *l1, ListNode *l2) {
        // 如果 有一个链表为空，则不需要合并，直接返回另外一个链表即可
        // 即使另外一个链表为空，那正好结果就是空
        if (l1 == NULL) {
            return l2;
        }
        if (l2 == NULL) {
            return l1;
        }

        // 合并两个链表
        dealChen(l1, l2);
        return headNode;
    }

    /**
     * 合并两个链表，
     * 定义 本节点为正在处理的节点
     * @param l1
     * @param l2
     */
    void dealChen(ListNode *l1, ListNode *l2) {
        // 首先设置头结点。根据 l1 链表和l2 链表头结点的值，确定哪个是头结点
        // 即哪个小，哪个就是头结点
        if (l1->val <= l2->val) {
            headNode = l1;
        } else {
            headNode = l2;
        }

        // 定义前置节点，初始时前置节点为空
        ListNode *preNode = NULL;
        // 如果两个链表都有值
        while (l1 != NULL && l2 != NULL) {
            // 如果  l1 链表的值较小，则选取本节点为 l1 节点
            // 否则选取本节点为 l2 节点
            if (l1->val <= l2->val) {
                // 前置节点不为空
                if (preNode != NULL) {
                    // 设置前置节点的下一个几点是本节点
                    preNode->next = l1;
                }
                // 进入下一个循环的时候，前置节点就是本节点
                preNode = l1;
                // 本节点处理完成，更新本节点为下一个节点，继续按照上述步骤处理
                l1 = l1->next;
            } else {
                // 前置节点不为空
                if (preNode != NULL) {
                    // 设置前置节点的下一个几点是本节点
                    preNode->next = l2;
                }
                // 进入下一个循环的时候，前置节点就是本节点
                preNode = l2;
                // 本节点处理完成，更新本节点为下一个节点，继续按照上述步骤处理
                l2 = l2->next;
            }
        }
        // 如果剩余的链表没有处理完成，则直接链接到 前置节点后面
        // 下面两个 if 语句最多只有一个可以执行
        if (l1 != NULL) {
            preNode->next = l1;
        }
        if (l2 != NULL) {
            preNode->next = l2;
        }
    }
};

int main() {
    ListNode *pNode11 = new ListNode(1);
    ListNode *pNode12 = new ListNode(2);
    ListNode *pNode13 = new ListNode(4);

    pNode11->next = pNode12;
    pNode12->next = pNode13;
    pNode13->next = NULL;

    ListNode *pNode21 = new ListNode(1);
    ListNode *pNode22 = new ListNode(3);
    ListNode *pNode23 = new ListNode(4);

    pNode21->next = pNode22;
    pNode22->next = pNode23;
    pNode23->next = NULL;

    Solution *pSolution = new Solution;
    ListNode *pNode = pSolution->mergeTwoLists(pNode11, pNode21);
    while (pNode != NULL) {
        cout << pNode->val << " ";
        pNode = pNode->next;
    }
    cout << endl;
    system("pause");
    return 0;
}