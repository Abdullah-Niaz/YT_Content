#include <bits/stdc++.h>
using namespace std;

int main()
{
    int *p = new int[8];
    //  0  = 1
    // 1  = 2
    for (int i = 0; i < 8; i++)
    {
        p[i] = i + 1;
    }
    // create an other array to point

    int *ptr = new int[13];

    for (int i = 0; i < 8; i++)
    {
        ptr[i] = p[i];
    }

    p = NULL;
    p = ptr;
    ptr = NULL;

    for (int i = 0; i < 7; i++)
    {
        cout << p[i] << " ";
    }
    return 0;
}