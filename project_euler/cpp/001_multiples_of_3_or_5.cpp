#include <iostream>
//Multiples of 3 and 5

int main()
{
  int sum;
  for(int i = 1; i < 1000; i++)
  {
    if (i % 5 == 0 || i % 3 == 0)
    {
      sum += i;
    }
  }
  std::cout << sum << std::endl;
  return 0;
}
