#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <iterator>
using namespace std;

std::string part2(const std::vector<int> &input)
{
    std::vector<int> l(input);
    int cnt = 0;
    int idx = 0;
    while ( idx < l.size() ) {
        int jmp = l[idx];
        if (jmp >= 3) {
            l[idx]--;
        } else {
            l[idx]++;
        }
        idx += jmp;
        cnt++;
    }
    std::stringstream sstr;
    sstr << cnt;
    return sstr.str(); 
}

int main()
{
    std::cout << part2(std::vector<int>( std::istream_iterator<int>(std::cin), std::istream_iterator<int>() )) << std::endl;
    return 0;
}
