ssing data filter(Remove data with missing Ref value)
 awk -F',' '$4' input > output  



 # Feature reduction, which will decrease 26 features into 6 features (Get mean of each feature of dfferent time in 1 hour)

 awk -F',' '{nu1=0;sum1=0;for(i=4;i<=7;i++){if($i){nu1++;sum1=sum1+$i}}  nu2=0;sum2=0;for(i=8;i<=11;i++){if($i){nu2++;sum2=sum2+$i}} nu3=0;sum3=0;for(i=12;i<=15;i++){if($i){nu3++;sum3=sum3+$i}} nu4=0;sum4=0;for(i=16;i<=19;i++){if($i){nu4++;sum4=sum4+$i}} nu5=0;sum5=0;for(i=20;i<=23;i++){if($i){nu5++;sum5=sum5+$i}} res = "";if(nu1){res = res " " sum1/nu1} else{res = res " 0"} if(nu2){res = res " " sum2/nu1}else{res = res " 0"} if(nu3){res = res " " sum3/nu1}else{res = res " 0"} if(nu4){res = res " " sum4/nu1} else{res = res " 0"} if(nu5){res = res " " sum5/nu1} else{res = res " 0"} print($1,$3,res)}' temp |more


