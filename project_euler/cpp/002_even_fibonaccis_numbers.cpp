#include <iostream>
// Even Fibonacci numbers
int main()
{
  int a0 = 1, a1 = 2;
  long int sum = a1;
  while(a1 <= 4000000)
  {
    int tmp = a1;
    a1 = a0 + a1; 
    a0 = tmp;
    if (a1 % 2 == 0)
    {
      sum += a1;
    }
  }
  std::cout << sum << std::endl;
  return 0;
}
