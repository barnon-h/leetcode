#include <unordered_map>

class Solution 
{

private:
    unordered_map <int, int> dict;
public:
    int tribonacci(int n) 
    {
        if( n == 0 ) return 0;
        if( n == 1 ) return 1;
        if( n == 2 ) return 1;

        if( dict.find( n ) != dict.end()){ return dict[ n ];}

        dict[ n ] = tribonacci( n - 3 ) + tribonacci( n - 2 ) + tribonacci( n - 1 );
        return dict[ n ] ;
    }
};