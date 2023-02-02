const  str = `@NF@]hO<OtXt!pA[]U#sUSI!:^O(II/@(#</HPwLg"@%KJg5"NG;>2JX2(ZO}Sp+=U]wR!i!M)!PvhH>LH"vA[Q{i5>NPg}T!q~s;_C&Dn6GBSA7[X=CL5TX#g)Qt,_FhFW3$VPX?q0$otLXdH*$~Kj,U<Oa#A.Y+)l~&IaM]EGVmD"WVbd;TDaI-uBrRL'LElMS).^BPGu>=ED^sB-<CeEG_,a])H[sX]FWtRQ]GR-?(R!K1XP{.>on.?KaSC')w[MBs|T=M&/L%DK^6TB3Z*?7>;T2PX((6}TG9`


const reg = /[-./0-9:a-z]/g

var arr = str.match(reg)

console.log(arr.join(''))