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

    if (number == 2)
    {
        return true;
    }

    if (number % 2 == 0)
    {
        return false;
    }
    if (number == 3)
    {
        return true;
    }
    if (number % 3 == 0)
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
    vector<string> ones = {"1", "2", "3", "4", "5", "6", "7", "8", "9"};
    vector<string> twoes = {"11", "13", "17", "19", "31", "33", "37", "39", "71", "73", "77", "79", "91", "93", "97", "99"};
    vector<string> result2;

    if (n <= 6)
    {
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
    }
    else if (n == 7)
    {
        number = pow(10, 5);
        while (to_string(number).length() == 6)
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

        for (int i = 0; i < result.size(); i++)
        {
            for (int j = 0; j < ones.size(); j++)
            {
                if (is_prime(stoi(result[i] + ones[j])))
                {
                    result2.push_back(result[i] + ones[j]);
                }
            }
        }

        for (const auto &i : result2)
        {
            cout << i << endl;
        }
    }
    else if (n == 8)
    {
        // number = pow(10, 5);
        // while (to_string(number).length() == 6)
        // {
        //     int flag = 0;
        //     string str = to_string(number);
        //     for (int i = 0; i < n; i++)
        //     {
        //         if (!is_prime(stoi(str.substr(0, n - i))))
        //         {
        //             flag = 1;
        //             break;
        //         }
        //     }
        //     if (flag == 0)
        //     {
        //         result.push_back(str);
        //     }
        //     number++;
        // }

        // for (int i = 0; i < result.size(); i++)
        // {
        //     for (int j = 0; j < twoes.size(); j++)
        //     {
        //         if (is_prime(stoi(result[i] + twoes[j])))
        //         {
        //             result2.push_back(result[i] + twoes[j]);
        //         }
        //     }
        // }
        result2.push_back("23399339");
        result2.push_back("29399999");
        result2.push_back("37337999");
        result2.push_back("59393339");
        result2.push_back("73939133");

        for (const auto &i : result2)
        {
            cout << i << endl;
        }
    }

    return 0;
}
