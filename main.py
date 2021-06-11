print("")
print("  * * * * *    * * * * *     **       * * * * *    * * * * *  ")
print("  *                *        *  *      *       *    *          ")
print("  * * * * *        *       ******     * * * * *    * * * * *  ")
print("          *        *      *      *    *     *              *  ")
print("  * * * * *        *     *        *   *       *    * * * * *  ")
print("")
num_rows = int(input("Enter the number of rows: "))
pattern = int(input("Enter 1 for True & 0 for False: "))
if pattern:
    for i in range(0, num_rows + 1):
        print("* " * i)
else:
    for i in range(num_rows, 0, -1):
        print("* " * i)
