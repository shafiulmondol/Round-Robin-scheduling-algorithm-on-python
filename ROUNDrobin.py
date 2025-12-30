n = int(input('Enter the number of process: '))

p = []
at = []
bt = []
rt = []
ct = [0]*n
tat = [0]*n
wt = [0]*n
que = []
gc = []
gct = [0]


print("Enter the process element:\n")
for i in range(n):
    p.append(input("Enter process: "))
    at.append(int(input(f'Enter arrival time for process {p[i]}: ')))
    bt.append(int(input(f'Enter burst time for process {p[i]}: ')))
    rt.append(bt[i])

tq = int(input('Enter time quantum: '))

# sort by arrival time
sortedp = sorted(range(n), key=lambda i: at[i])
time=0

gct[0] = time

# add first process
first = sortedp[0]      # index of first arriving process
que.append(first)       # add to queue

visited = [False] * n   # no process visited yet
visited[first] = True   # mark first process as visited


j = 0

while que:
    i = que.pop(0)     # process index
    gc.append(p[i])

    if rt[i] >= tq:
        time += tq
        rt[i] -= tq
    else:
        time += rt[i]
        rt[i] = 0

    gct.append(time)
    j += 1

    # add newly arrived processes
    for k in range(n):
        if at[k] <= time and not visited[k]:
            que.append(k)
            visited[k] = True

    # reinsert if not finished
    if rt[i] > 0:
        que.append(i)

completed = [False]*n
leng = len(gc)

for i in range(n):
    for t in range(leng):
        if gc[t] == p[i]:
            ct[i] = gct[t+1]   # overwrite → last occurrence
            completed[i] = True


for i in range(n):
    tat[i] = ct[i] - at[i]
    wt[i] = tat[i] - bt[i]

# output
print("\nProcess AT BT CT TAT WT")
for i in range(n):
    print(p[i], at[i], bt[i], ct[i], tat[i], wt[i])

print("\nQueue:")
for x in gc:
    print(f"| {x} ", end="")
print("|")
print("\nGantt Chart:")
for x in gc:
    print(f"| {x} ", end="")
print("|")

for t in gct:
    print(t, end="   ")
print()

