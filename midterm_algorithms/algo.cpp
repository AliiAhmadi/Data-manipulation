#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

bool is_prime(int number)
{
    if (number == 1)
    {
        return false;
    }
    int flag = 0;
    for (int k = 2; k <= sqrt(number); k++)
    {
        if (number % k == 0)
        {
            flag = 1;
            break;
        }
    }
    if (flag == 0)
    {
        return true;
    }
    return false;
}

int main()
{
    int n;
    cin >> n;

    int number = pow(10, n - 1);

    vector<string> result;

    while (to_string(number).length() == n)
    {
        int flag = 0;
        string str = to_string(number);
        for (int i = 0; i < n; i++)
        {
            if (!is_prime(stoi(str.substr(0, n - i))))
            {
                flag = 1;
                break;
            }
        }
        if (flag == 0)
        {
            result.push_back(str);
        }
        number++;
    }

    for (const auto &i : result)
    {
        cout << i << endl;
    }

    return 0;
}
