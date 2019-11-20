#include <bits/stdc++.h>
#include "socialnetwork.h"

using namespace std;

extern Graph Node_Properties[MAX_NODES];

int main() {
  //freopen("datasets/fb/facebook_combined-small.in","r",stdin);
  // freopen("Results.out","w",stdout);
  freopen("Algo.out","w",stdout);

  clock_t start, end;
  scangraph();

  cout<<"FINDING TOP 10 INFLUENTIAL NODES\n\n";

  cout<<"\nDEGREE_CENTRALITY"<<endl;
  start = clock();
  degree_centrality();
  end= clock();
  cout<< ((float)end-(float)start)/CLOCKS_PER_SEC<<"sec"<<endl;


  cout<<"\nLOCAL_DEGREE_CENTRALITY"<<endl;
  start = clock();
  local_degree_centrality();
  end= clock();
  cout<< ((float)end-(float)start)/CLOCKS_PER_SEC<<"sec"<<endl;

  // cout<<"BETWEENNESS_CENTRALITY"<<endl;
  // start = clock();
  // betweenness_centrality();
  // end= clock();
  // cout<< ((float)end-(float)start)/CLOCKS_PER_SEC<<"sec"<<endl;


  cout<<"\nCLOSENESS_CENTRALITY"<<endl;
  start = clock();
  closeness_centrality();
  end= clock();
  cout<< ((float)end-(float)start)/CLOCKS_PER_SEC<<"sec"<<endl;


  cout<<"\nPAGERANK_CENTRALITY"<<endl;
  start = clock();
  pagerank_centrality();
  end= clock();
  cout<< ((float)end-(float)start)/CLOCKS_PER_SEC<<"sec"<<endl;


  cout<<"\nKSHELL_CENTRALITY"<<endl;
  start = clock();
  kshell_centrality();
  end= clock();
  cout<< ((float)end-(float)start)/CLOCKS_PER_SEC<<"sec"<<endl;
  // cascade_DC();
  // cascade_LDC();
  // cascade_BC();
  // cascade_CC();
  // cascade_PR();
  // cascade_KS();

  return 0;
}
