

class Solution 
{
public:
    int tribonacci( int n ) 
    {
        if( n == 0 ) return 0;
        if( n == 1 ) return 1;
        if( n == 2 ) return 1;

        vector<int> table( n + 1 );
        table[ 0 ] = 0;
        table[ 1 ] = 1;
        table[ 2 ] = 1;
        
        for( int i = 3; i <= n; i++ )
        {
            table[ i ] = table[ i - 1 ] + table[ i - 2 ] + table[ i - 3 ];
        }
        
        return table[ n ] ;
    }
};