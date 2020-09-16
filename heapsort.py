def heap_sort(arr, n):
    # arr[0]은 사용하지 않고 a[1:n]의 원소를 오름차순으로 정렬
    for i in range(n//2, 0, -1):    # 배열 arr[]을 히프로 변환
        heapify(arr, i, n)
    for i in range(n-1, 0, -1):  # 배열 arr[]을 오름차순으로 정렬
        arr[1], arr[i+1] = arr[i+1], arr[1]  # a[1]은 제일 큰 원소
        heapify(arr, 1, i)


def heapify(arr, h, m):
    # 루트 h를 제외한 h의 왼쪽 서브트리와 오른쪽 서브트리는 히프
    # 현재 시점으로 노드의 최대 레벨 순서 번호는 m
    v = arr[h]
    j = 2*h
    while j <= m:
        if j < m and arr[j] < arr[j+1]:
            j += 1  # j는 값이 큰 왼쪽 또는 오른쪽 자식 노드
        if v >= arr[j]:
            break
        else:
            arr[j//2] = arr[j]  # a[j]를 부모 노드로 이동
        j *= 2
    arr[j//2] = v
