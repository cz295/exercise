
#include <iostream>
#include <math.h>
#include <list>
// Largest prime factor
int find_max_prime_factor(const long int m)
{
  std::list <int> prime_list {2, 3};
  int largest_prime = 1, start = 3;
  long int n = m;
  if(n <= 3)
    return n;
  while (n % 2 == 0)
  {
    n = n / 2;
    largest_prime = 2;
  }
  while (n % 3 == 0)
  {
    n = n / 3;
    largest_prime = 3;
  }
  while(true)
  {
    start += 2;
    bool prime = true;
    for (std::list<int>::iterator it = prime_list.begin(); it != prime_list.end(); it++)
    {
      if (start % *it == 0)
        prime = false;
    }
    if(prime)
    {
      prime_list.push_back(start);
      while (n % start == 0)
      {
        n = n / start;
        largest_prime = start;
      }
    }
    if (n == 1)
      break;
  }
  return largest_prime;
}

int main()
{
  long int num = 600851475143;
  std::cout << find_max_prime_factor(num) << std::endl;
  return 0;
}
