#include<bits/stdc++.h>
using namespace std;
int dp[100010],bj[100010],vis[100010];
int  ans;
struct node
{
    int x,y;
    friend bool operator <(node a,node b)
    {
        return  a.x<b.x;
    }
} ft,et;

int pd(int h)
{
    for(int i=2; i*i<=h; i++)
        if(h%i==0) return 0;
    return 1;
}


void solve(int n)
{
    ans=0;
    priority_queue<node>qe;
    ft.x=n,ft.y=0;
    qe.push(ft);
    while(!qe.empty())
    {
        ft=qe.top();
        qe.pop();
        if(ft.y<dp[ft.x])
            continue;
        if(vis[ft.x]||ft.x<=1)//如果是质数或者小于一就只能停止了
        {
            ans=max(ans,ft.y);
            continue;
        }

        for(int i=1; bj[i]*bj[i]<=ft.x; i++)//
        {
            if(ft.x%bj[i]==0)//bj[i]不能为零否则运行出错
            {
                et.x=ft.x-2*bj[i];
                et.y=ft.y+bj[i];
                if(dp[et.x]<et.y)
                {
                dp[et.x]=et.y;
                qe.push(et);
                }
            }
        }
    }
}

int main()
{
    memset(bj,0,sizeof(bj));
    memset(vis,0,sizeof(vis));
    int k=1;
    for(int i=2; i*i<=101000; i++)//多一个质数出来
    {
        if(pd(i))
        {
            bj[k++]=i;
            vis[i]=1;//记录质数
        }
    }

    int n;
    while(scanf("%d",&n)!=EOF)
    {
        memset(dp,0,sizeof(dp));
        solve(n);
        printf("%d\n",ans);
    }
    return 0;
}