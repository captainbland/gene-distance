tsst1 = """ctcaaagata gattgaccag cgatgtttaa agtcatattt cacggatcca catttacgat
      aaacatatct agttacacaa tattatccct tactgcaaca caggacgttt ctcagcgtaa
      aaaacaccac tagaaagtga ctttaaagaa tataactaat tcaaacttat attaattaat
      attctttaaa tgaccactca cactttgttt tttgctattt gtaactttaa aatgttgttt
      aaatctatat tttttttgat atagctccct atgtaacaaa cactttttaa ttaatatata
      tttaaacaat aatttagaga tggttaattg attcatttaa ataatattta tacattctat
      atgtaaacgt ttacacattt gaatgaagga gaattaaaa
"""

tsst2 = """tatagccctg cttttacaaa aggggaaaaa gttgacttaa acacaaaaag aactaaaaaa
        agccaacata ctagcgaagg aacttatatc catttccaaa taagtggcgt tacaaatact
       gaaaaattac ctactccaat agaactacct ttaaaagtta aggttcatgg taaagatagc
       cccttaaagt attggccaaa gttcgataaa aaacaattag ctatatcaac tttagacttt
       gaaattcgtc atcagctaac tcaaatacat ggattatatc gttcaagcga taaaacgggt
       ggttattgga aaat
"""

mat_peptide = """
11111agtggtttt agaaaaatgg cattcccatc
     tggtaaagtt gagggttgta tggtacaagt aacttgtggt acaactacac ttaacggtct
     ttggcttgat gacgttgttt actgtccaag acatgtgatc tgcacctctg aagacatgct
     taaccctaat tatgaagatt tactcattcg taagtctaat cataatttct tggtacaggc
"""

sars_cov_2 = """
        1 attaaaggtt tataccttcc caggtaacaa accaaccaac tttcgatctc ttgtagatct
        gttctctaaa cgaactttaa aatctgtgtg gctgtcactc ggctgcatgc ttagtgcact
       cacgcagtat aattaataac taattactgt cgttgacagg acacgagtaa ctcgtctatc
       ttctgcaggc tgcttacggt ttcgtccgtg ttgcagccga tcatcagcac atctaggttt
       cgtccgggtg tgaccgaaag gtaagatgga gagccttgtc cctggtttca acgagaaaac
       acacgtccaa ctcagtttgc ctgttttaca ggttcgcgac gtgctcgtac gtggctttgg
       agactccgtg gaggaggtct tatcagaggc acgtcaacat cttaaagatg gcacttgtgg
       cttagtagaa gttgaaaaag gcgttttgcc tcaacttgaa cagccctatg tgttcatcaa
       acgttcggat gctcgaactg cacctcatgg tcatgttatg gttgagctgg tagcagaact
       cgaaggcatt cagtacggtc gtagtggtga gacacttggt gtccttgtcc ctcatgtggg
       cgaaatacca gtggcttacc gcaaggttct tcttcgtaag aacggtaata aaggagctgg
       tggccatagt tacggcgccg atctaaagtc atttgactta ggcgacgagc ttggcactga
       tccttatgaa gattttcaag aaaactggaa cactaaacat agcagtggtg ttacccgtga
       actcatgcgt gagcttaacg gaggggcata cactcgctat gtcgataaca acttctgtgg
       ccctgatggc taccctcttg agtgcattaa agaccttcta gcacgtgctg gtaaagcttc
       atgcactttg tccgaacaac tggactttat tgacactaag aggggtgtat actgctgccg
       tgaacatgag catgaaattg cttggtacac ggaacgttct gaaaagagct atgaattgca
      gacacctttt gaaattaaat tggcaaagaa atttgacacc ttcaatgggg aatgtccaaa
      ttttgtattt cccttaaatt ccataatcaa gactattcaa ccaagggttg aaaagaaaaa
      gcttgatggc tttatgggta gaattcgatc tgtctatcca gttgcgtcac caaatgaatg
      caaccaaatg tgcctttcaa ctctcatgaa gtgtgatcat tgtggtgaaa cttcatggca
      gacgggcgat tttgttaaag ccacttgcga attttgtggc actgagaatt tgactaaaga
      aggtgccact acttgtggtt acttacccca aaatgctgtt gttaaaattt attgtccagc
      atgtcacaat tcagaagtag gacctgagca tagtcttgcc gaataccata aatctggctt
      gaaaaccatt cttcgtaagg gtggtcgcac tattgccttt ggaggctgtg tgttctctta
      tgttggttgc cataacaagt gtgcctattg ggttccacgt gctagcgcta acataggttg
      taaccataca ggtgttgttg gagaaggttc cgaaggtctt aatgacaacc ttcttgaaat
      actccaaaaa gagaaagtca acatcaatat tgttggtgac tttaaactta atgaagagat
      cgccattatt ttggcatctt tttctgcttc cacaagtgct tttgtggaaa ctgtgaaagg
      tttggattat aaagcattca aacaaattgt tgaatcctgt ggtaatttta aagttacaaa
      aggaaaagct aaaaaaggtg cctggaatat tggtgaacag aaatcaatac tgagtcctct
      ttatgcattt gcatcagagg ctgctcgtgt tgtacgatca attttctccc gcactcttga
      aactgctcaa aattctgtgc gtgttttaca gaaggccgct ataacaatac tagatggaat
      ttcacagtat tcactgagac tcattgatgc tatgatgttc acatctgatt tggctactaa
      caatctagtt gtaatggcct acattacagg tggtgttgtt cagttgactt cgcagtggct
      aactaacatc tttggcactg tttatgaaaa actcaaaccc gtccttgatt ggcttgaaga
      gaagtttaag gaaggtgtag agtttcttag agacggttgg gaaattgtta aatttatctc
      aacctgtgct tgtgaaattg tcggtggaca aattgtcacc tgtgcaaagg aaattaagga
      gagtgttcag acattcttta agcttgtaaa taaatttttg gctttgtgtg ctgactctat
      cattattggt ggagctaaac ttaaagcctt gaatttaggt gaaacatttg tcacgcactc
      aaagggattg tacagaaagt gtgttaaatc cagagaagaa actggcctac tcatgcctct
      aaaagcccca aaagaaatta tcttcttaga gggagaaaca cttcccacag aagtgttaac
      agaggaagtt gtcttgaaaa ctggtgattt acaaccatta gaacaaccta ctagtgaagc
      tgttgaagct ccattggttg gtacaccagt ttgtattaac gggcttatgt tgctcgaaat
      caaagacaca gaaaagtact gtgcccttgc acctaatatg atggtaacaa acaatacctt
      cacactcaaa ggcggtgcac caacaaaggt tacttttggt gatgacactg tgatagaagt
      gcaaggttac aagagtgtga atatcacttt tgaacttgat gaaaggattg ataaagtact
      taatgagaag tgctctgcct atacagttga actcggtaca gaagtaaatg agttcgcctg
      tgttgtggca gatgctgtca taaaaacttt gcaaccagta tctgaattac ttacaccact
      gggcattgat ttagatgagt ggagtatggc tacatactac ttatttgatg agtctggtga
      gtttaaattg gcttcacata tgtattgttc tttctaccct ccagatgagg atgaagaaga
      aggtgattgt gaagaagaag agtttgagcc atcaactcaa tatgagtatg gtactgaaga
      tgattaccaa ggtaaacctt tggaatttgg tgccacttct gctgctcttc aacctgaaga
      agagcaagaa gaagattggt tagatgatga tagtcaacaa actgttggtc aacaagacgg
      cagtgaggac aatcagacaa ctactattca aacaattgtt gaggttcaac ctcaattaga
      gatggaactt acaccagttg ttcagactat tgaagtgaat agttttagtg gttatttaaa
      acttactgac aatgtataca ttaaaaatgc agacattgtg gaagaagcta aaaaggtaaa
      accaacagtg gttgttaatg cagccaatgt ttaccttaaa catggaggag gtgttgcagg
      agccttaaat aaggctacta acaatgccat gcaagttgaa tctgatgatt acatagctac
      taatggacca cttaaagtgg gtggtagttg tgttttaagc ggacacaatc ttgctaaaca
      ctgtcttcat gttgtcggcc caaatgttaa caaaggtgaa gacattcaac ttcttaagag
      tgcttatgaa aattttaatc agcacgaagt tctacttgca ccattattat cagctggtat
      ttttggtgct gaccctatac attctttaag agtttgtgta gatactgttc gcacaaatgt
      ctacttagct gtctttgata aaaatctcta tgacaaactt gtttcaagct ttttggaaat
      gaagagtgaa aagcaagttg aacaaaagat cgctgagatt cctaaagagg aagttaagcc
      atttataact gaaagtaaac cttcagttga acagagaaaa caagatgata agaaaatcaa
      agcttgtgtt gaagaagtta caacaactct ggaagaaact aagttcctca cagaaaactt
      gttactttat attgacatta atggcaatct tcatccagat tctgccactc ttgttagtga
      cattgacatc actttcttaa agaaagatgc tccatatata gtgggtgatg ttgttcaaga
      gggtgtttta actgctgtgg ttatacctac taaaaaggct ggtggcacta ctgaaatgct
      agcgaaagct ttgagaaaag tgccaacaga caattatata accacttacc cgggtcaggg
      tttaaatggt tacactgtag aggaggcaaa gacagtgctt aaaaagtgta aaagtgcctt
      ttacattcta ccatctatta tctctaatga gaagcaagaa attcttggaa ctgtttcttg
      gaatttgcga gaaatgcttg cacatgcaga agaaacacgc aaattaatgc ctgtctgtgt
      ggaaactaaa gccatagttt caactataca gcgtaaatat aagggtatta aaatacaaga
      gggtgtggtt gattatggtg ctagatttta cttttacacc agtaaaacaa ctgtagcgtc
      acttatcaac acacttaacg atctaaatga aactcttgtt acaatgccac ttggctatgt
      aacacatggc ttaaatttgg aagaagctgc tcggtatatg agatctctca aagtgccagc
      tacagtttct gtttcttcac ctgatgctgt tacagcgtat aatggttatc ttacttcttc
      ttctaaaaca cctgaagaac attttattga aaccatctca cttgctggtt cctataaaga
      ttggtcctat tctggacaat ctacacaact aggtatagaa tttcttaaga gaggtgataa
      aagtgtatat tacactagta atcctaccac attccaccta gatggtgaag ttatcacctt
      tgacaatctt aagacacttc tttctttgag agaagtgagg actattaagg tgtttacaac
      agtagacaac attaacctcc acacgcaagt tgtggacatg tcaatgacat atggacaaca
      gtttggtcca acttatttgg atggagctga tgttactaaa ataaaacctc ataattcaca
      tgaaggtaaa acattttatg ttttacctaa tgatgacact ctacgtgttg aggcttttga
      gtactaccac acaactgatc ctagttttct gggtaggtac atgtcagcat taaatcacac
      taaaaagtgg aaatacccac aagttaatgg tttaacttct attaaatggg cagataacaa
      ctgttatctt gccactgcat tgttaacact ccaacaaata gagttgaagt ttaatccacc
      tgctctacaa gatgcttatt acagagcaag ggctggtgaa gctgctaact tttgtgcact
      tatcttagcc tactgtaata agacagtagg tgagttaggt gatgttagag aaacaatgag
      ttacttgttt caacatgcca atttagattc ttgcaaaaga gtcttgaacg tggtgtgtaa
      aacttgtgga caacagcaga caacccttaa gggtgtagaa gctgttatgt acatgggcac
      actttcttat gaacaattta agaaaggtgt tcagatacct tgtacgtgtg gtaaacaagc
      tacaaaatat ctagtacaac aggagtcacc ttttgttatg atgtcagcac cacctgctca
      gtatgaactt aagcatggta catttacttg tgctagtgag tacactggta attaccagtg
      tggtcactat aaacatataa cttctaaaga aactttgtat tgcatagacg gtgctttact
      tacaaagtcc tcagaataca aaggtcctat tacggatgtt ttctacaaag aaaacagtta
      cacaacaacc ataaaaccag ttacttataa attggatggt gttgtttgta cagaaattga
      ccctaagttg gacaattatt ataagaaaga caattcttat ttcacagagc aaccaattga
      tcttgtacca aaccaaccat atccaaacgc aagcttcgat aattttaagt ttgtatgtga
      taatatcaaa tttgctgatg atttaaacca gttaactggt tataagaaac ctgcttcaag
      agagcttaaa gttacatttt tccctgactt aaatggtgat gtggtggcta ttgattataa
      acactacaca ccctctttta agaaaggagc taaattgtta cataaaccta ttgtttggca
      tgttaacaat gcaactaata aagccacgta taaaccaaat acctggtgta tacgttgtct
      ttggagcaca aaaccagttg aaacatcaaa ttcgtttgat gtactgaagt cagaggacgc
      gcagggaatg gataatcttg cctgcgaaga tctaaaacca gtctctgaag aagtagtgga
      aaatcctacc atacagaaag acgttcttga gtgtaatgtg aaaactaccg aagttgtagg
      agacattata cttaaaccag caaataatag tttaaaaatt acagaagagg ttggccacac
      agatctaatg gctgcttatg tagacaattc tagtcttact attaagaaac ctaatgaatt
      atctagagta ttaggtttga aaacccttgc tactcatggt ttagctgctg ttaatagtgt
      cccttgggat actatagcta attatgctaa gccttttctt aacaaagttg ttagtacaac
      tactaacata gttacacggt gtttaaaccg tgtttgtact aattatatgc cttatttctt
      tactttattg ctacaattgt gtacttttac tagaagtaca aattctagaa ttaaagcatc
      tatgccgact actatagcaa agaatactgt taagagtgtc ggtaaatttt gtctagaggc
      ttcatttaat tatttgaagt cacctaattt ttctaaactg ataaatatta taatttggtt
      tttactatta agtgtttgcc taggttcttt aatctactca accgctgctt taggtgtttt
      aatgtctaat ttaggcatgc cttcttactg tactggttac agagaaggct atttgaactc
      tactaatgtc actattgcaa cctactgtac tggttctata ccttgtagtg tttgtcttag
      tggtttagat tctttagaca cctatccttc tttagaaact atacaaatta ccatttcatc
      ttttaaatgg gatttaactg cttttggctt agttgcagag tggtttttgg catatattct
      tttcactagg tttttctatg tacttggatt ggctgcaatc atgcaattgt ttttcagcta
      ttttgcagta cattttatta gtaattcttg gcttatgtgg ttaataatta atcttgtaca
      aatggccccg atttcagcta tggttagaat gtacatcttc tttgcatcat tttattatgt
      atggaaaagt tatgtgcatg ttgtagacgg ttgtaattca tcaacttgta tgatgtgtta
      caaacgtaat agagcaacaa gagtcgaatg tacaactatt gttaatggtg ttagaaggtc
      cttttatgtc tatgctaatg gaggtaaagg cttttgcaaa ctacacaatt ggaattgtgt
      taattgtgat acattctgtg ctggtagtac atttattagt gatgaagttg cgagagactt
      gtcactacag tttaaaagac caataaatcc tactgaccag tcttcttaca tcgttgatag
      tgttacagtg aagaatggtt ccatccatct ttactttgat aaagctggtc aaaagactta
      tgaaagacat tctctctctc attttgttaa cttagacaac ctgagagcta ataacactaa
      aggttcattg cctattaatg ttatagtttt tgatggtaaa tcaaaatgtg aagaatcatc
      tgcaaaatca gcgtctgttt actacagtca gcttatgtgt caacctatac tgttactaga
      tcaggcatta gtgtctgatg ttggtgatag tgcggaagtt gcagttaaaa tgtttgatgc
      ttacgttaat acgttttcat caacttttaa cgtaccaatg gaaaaactca aaacactagt
      tgcaactgca gaagctgaac ttgcaaagaa tgtgtcctta gacaatgtct tatctacttt
      tatttcagca gctcggcaag ggtttgttga ttcagatgta gaaactaaag atgttgttga
      atgtcttaaa ttgtcacatc aatctgacat agaagttact ggcgatagtt gtaataacta
      tatgctcacc tataacaaag ttgaaaacat gacaccccgt gaccttggtg cttgtattga
      ctgtagtgcg cgtcatatta atgcgcaggt agcaaaaagt cacaacattg ctttgatatg
      gaacgttaaa gatttcatgt cattgtctga acaactacga aaacaaatac gtagtgctgc
      taaaaagaat aacttacctt ttaagttgac atgtgcaact actagacaag ttgttaatgt
      tgtaacaaca aagatagcac ttaagggtgg taaaattgtt aataattggt tgaagcagtt
      aattaaagtt acacttgtgt tcctttttgt tgctgctatt ttctatttaa taacacctgt
      tcatgtcatg tctaaacata ctgacttttc aagtgaaatc ataggataca aggctattga
      tggtggtgtc actcgtgaca tagcatctac agatacttgt tttgctaaca aacatgctga
      ttttgacaca tggtttagcc agcgtggtgg tagttatact aatgacaaag cttgcccatt
      gattgctgca gtcataacaa gagaagtggg ttttgtcgtg cctggtttgc ctggcacgat
      attacgcaca actaatggtg actttttgca tttcttacct agagttttta gtgcagttgg
      taacatctgt tacacaccat caaaacttat agagtacact gactttgcaa catcagcttg
      tgttttggct gctgaatgta caatttttaa agatgcttct ggtaagccag taccatattg
      ttatgatacc aatgtactag aaggttctgt tgcttatgaa agtttacgcc ctgacacacg
      ttatgtgctc atggatggct ctattattca atttcctaac acctaccttg aaggttctgt
      tagagtggta acaacttttg attctgagta ctgtaggcac ggcacttgtg aaagatcaga
      agctggtgtt tgtgtatcta ctagtggtag atgggtactt aacaatgatt attacagatc
      tttaccagga gttttctgtg gtgtagatgc tgtaaattta cttactaata tgtttacacc
      actaattcaa cctattggtg ctttggacat atcagcatct atagtagctg gtggtattgt
      agctatcgta gtaacatgcc ttgcctacta ttttatgagg tttagaagag cttttggtga
      atacagtcat gtagttgcct ttaatacttt actattcctt atgtcattca ctgtactctg
      tttaacacca gtttactcat tcttacctgg tgtttattct gttatttact tgtacttgac
      attttatctt actaatgatg tttctttttt agcacatatt cagtggatgg ttatgttcac
      acctttagta cctttctgga taacaattgc ttatatcatt tgtatttcca caaagcattt
      ctattggttc tttagtaatt acctaaagag acgtgtagtc tttaatggtg tttcctttag
      tacttttgaa gaagctgcgc tgtgcacctt tttgttaaat aaagaaatgt atctaaagtt
      gcgtagtgat gtgctattac ctcttacgca atataataga tacttagctc tttataataa
      gtacaagtat tttagtggag caatggatac aactagctac agagaagctg cttgttgtca
      tctcgcaaag gctctcaatg acttcagtaa ctcaggttct gatgttcttt accaaccacc
     acaaacctct atcacctcag ctgttttgca gagtggtttt agaaaaatgg cattcccatc
     tggtaaagtt gagggttgta tggtacaagt aacttgtggt acaactacac ttaacggtct
     ttggcttgat gacgtagttt actgtccaag acatgtgatc tgcacctctg aagacatgct
     taaccctaat tatgaagatt tactcattcg taagtctaat cataatttct tggtacaggc
     tggtaatgtt caactcaggg ttattggaca ttctatgcaa aattgtgtac ttaagcttaa
     ggttgataca gccaatccta agacacctaa gtataagttt gttcgcattc aaccaggaca
     gactttttca gtgttagctt gttacaatgg ttcaccatct ggtgtttacc aatgtgctat
     gaggcccaat ttcactatta agggttcatt ccttaatggt tcatgtggta gtgttggttt
     taacatagat tatgactgtg tctctttttg ttacatgcac catatggaat taccaactgg
     agttcatgct ggcacagact tagaaggtaa cttttatgga ccttttgttg acaggcaaac
     agcacaagca gctggtacgg acacaactat tacagttaat gttttagctt ggttgtacgc
     tgctgttata aatggagaca ggtggtttct caatcgattt accacaactc ttaatgactt
     taaccttgtg gctatgaagt acaattatga acctctaaca caagaccatg ttgacatact
     aggacctctt tctgctcaaa ctggaattgc cgttttagat atgtgtgctt cattaaaaga
     attactgcaa aatggtatga atggacgtac catattgggt agtgctttat tagaagatga
     atttacacct tttgatgttg ttagacaatg ctcaggtgtt actttccaaa gtgcagtgaa
     aagaacaatc aagggtacac accactggtt gttactcaca attttgactt cacttttagt
     tttagtccag agtactcaat ggtctttgtt cttttttttg tatgaaaatg cctttttacc
     ttttgctatg ggtattattg ctatgtctgc ttttgcaatg atgtttgtca aacataagca
     tgcatttctc tgtttgtttt tgttaccttc tcttgccact gtagcttatt ttaatatggt
     ctatatgcct gctagttggg tgatgcgtat tatgacatgg ttggatatgg ttgatactag
     tttgtctggt tttaagctaa aagactgtgt tatgtatgca tcagctgtag tgttactaat
     ccttatgaca gcaagaactg tgtatgatga tggtgctagg agagtgtgga cacttatgaa
     tgtcttgaca ctcgtttata aagtttatta tggtaatgct ttagatcaag ccatttccat
     gtgggctctt ataatctctg ttacttctaa ctactcaggt gtagttacaa ctgtcatgtt
     tttggccaga ggtattgttt ttatgtgtgt tgagtattgc cctattttct tcataactgg
     taatacactt cagtgtataa tgctagttta ttgtttctta ggctattttt gtacttgtta
     ctttggcctc ttttgtttac tcaaccgcta ctttagactg actcttggtg tttatgatta
     cttagtttct acacaggagt ttagatatat gaattcacag ggactactcc cacccaagaa
     tagcatagat gccttcaaac tcaacattaa attgttgggt gttggtggca aaccttgtat
     caaagtagcc actgtacagt ctaaaatgtc agatgtaaag tgcacatcag tagtcttact
     ctcagttttg caacaactca gagtagaatc atcatctaaa ttgtgggctc aatgtgtcca
     gttacacaat gacattctct tagctaaaga tactactgaa gcctttgaaa aaatggtttc
     actactttct gttttgcttt ccatgcaggg tgctgtagac ataaacaagc tttgtgaaga
     aatgctggac aacagggcaa ccttacaagc tatagcctca gagtttagtt cccttccatc
     atatgcagct tttgctactg ctcaagaagc ttatgagcag gctgttgcta atggtgattc
     tgaagttgtt cttaaaaagt tgaagaagtc tttgaatgtg gctaaatctg aatttgaccg
     tgatgcagcc atgcaacgta agttggaaaa gatggctgat caagctatga cccaaatgta
     taaacaggct agatctgagg acaagagggc aaaagttact agtgctatgc agacaatgct
     tttcactatg cttagaaagt tggataatga tgcactcaac aacattatca acaatgcaag
     agatggttgt gttcccttga acataatacc tcttacaaca gcagccaaac taatggttgt
     cataccagac tataacacat ataaaaatac gtgtgatggt acaacattta cttatgcatc
     agcattgtgg gaaatccaac aggttgtaga tgcagatagt aaaattgttc aacttagtga
     aattagtatg gacaattcac ctaatttagc atggcctctt attgtaacag ctttaagggc
     caattctgct gtcaaattac agaataatga gcttagtcct gttgcactac gacagatgtc
     ttgtgctgcc ggtactacac aaactgcttg cactgatgac aatgcgttag cttactacaa
     cacaacaaag ggaggtaggt ttgtacttgc actgttatcc gatttacagg atttgaaatg
     ggctagattc cctaagagtg atggaactgg tactatctat acagaactgg aaccaccttg
     taggtttgtt acagacacac ctaaaggtcc taaagtgaag tatttatact ttattaaagg
     attaaacaac ctaaatagag gtatggtact tggtagttta gctgccacag tacgtctaca
     agctggtaat gcaacagaag tgcctgccaa ttcaactgta ttatctttct gtgcttttgc
     tgtagatgct gctaaagctt acaaagatta tctagctagt gggggacaac caatcactaa
     ttgtgttaag atgttgtgta cacacactgg tactggtcag gcaataacag ttacaccgga
     agccaatatg gatcaagaat cctttggtgg tgcatcgtgt tgtctgtact gccgttgcca
     catagatcat ccaaatccta aaggattttg tgacttaaaa ggtaagtatg tacaaatacc
     tacaacttgt gctaatgacc ctgtgggttt tacacttaaa aacacagtct gtaccgtctg
     cggtatgtgg aaaggttatg gctgtagttg tgatcaactc cgcgaaccca tgcttcagtc
     agctgatgca caatcgtttt taaacgggtt tgcggtgtaa gtgcagcccg tcttacaccg
     tgcggcacag gcactagtac tgatgtcgta tacagggctt ttgacatcta caatgataaa
     gtagctggtt ttgctaaatt cctaaaaact aattgttgtc gcttccaaga aaaggacgaa
     gatgacaatt taattgattc ttactttgta gttaagagac acactttctc taactaccaa
     catgaagaaa caatttataa tttacttaag gattgtccag ctgttgctaa acatgacttc
     tttaagttta gaatagacgg tgacatggta ccacatatat cacgtcaacg tcttactaaa
     tacacaatgg cagacctcgt ctatgcttta aggcattttg atgaaggtaa ttgtgacaca
     ttaaaagaaa tacttgtcac atacaattgt tgtgatgatg attatttcaa taaaaaggac
     tggtatgatt ttgtagaaaa cccagatata ttacgcgtat acgccaactt aggtgaacgt
     gtacgccaag ctttgttaaa aacagtacaa ttctgtgatg ccatgcgaaa tgctggtatt
     gttggtgtac tgacattaga taatcaagat ctcaatggta actggtatga tttcggtgat
     ttcatacaaa ccacgccagg tagtggagtt cctgttgtag attcttatta ttcattgtta
     atgcctatat taaccttgac cagggcttta actgcagagt cacatgttga cactgactta
     acaaagcctt acattaagtg ggatttgtta aaatatgact tcacggaaga gaggttaaaa
     ctctttgacc gttattttaa atattgggat cagacatacc acccaaattg tgttaactgt
     ttggatgaca gatgcattct gcattgtgca aactttaatg ttttattctc tacagtgttc
     ccacctacaa gttttggacc actagtgaga aaaatatttg ttgatggtgt tccatttgta
     gtttcaactg gataccactt cagagagcta ggtgttgtac ataatcagga tgtaaactta
     catagctcta gacttagttt taaggaatta cttgtgtatg ctgctgaccc tgctatgcac
     gctgcttctg gtaatctatt actagataaa cgcactacgt gcttttcagt agctgcactt
     actaacaatg ttgcttttca aactgtcaaa cccggtaatt ttaacaaaga cttctatgac
     tttgctgtgt ctaagggttt ctttaaggaa ggaagttctg ttgaattaaa acacttcttc
     tttgctcagg atggtaatgc tgctatcagc gattatgact actatcgtta taatctacca
     acaatgtgtg atatcagaca actactattt gtagttgaag ttgttgataa gtactttgat
     tgttacgatg gtggctgtat taatgctaac caagtcatcg tcaacaacct agacaaatca
     gctggttttc catttaataa atggggtaag gctagacttt attatgattc aatgagttat
     gaggatcaag atgcactttt cgcatataca aaacgtaatg tcatccctac tataactcaa
     atgaatctta agtatgccat tagtgcaaag aatagagctc gcaccgtagc tggtgtctct
     atctgtagta ctatgaccaa tagacagttt catcaaaaat tattgaaatc aatagccgcc
     actagaggag ctactgtagt aattggaaca agcaaattct atggtggttg gcacaacatg
     ttaaaaactg tttatagtga tgtagaaaac cctcacctta tgggttggga ttatcctaaa
     tgtgatagag ccatgcctaa catgcttaga attatggcct cacttgttct tgctcgcaaa
     catacaacgt gttgtagctt gtcacaccgt ttctatagat tagctaatga gtgtgctcaa
     gtattgagtg aaatggtcat gtgtggcggt tcactatatg ttaaaccagg tggaacctca
     tcaggagatg ccacaactgc ttatgctaat agtgttttta acatttgtca agctgtcacg
     gccaatgtta atgcactttt atctactgat ggtaacaaaa ttgccgataa gtatgtccgc
     aatttacaac acagacttta tgagtgtctc tatagaaata gagatgttga cacagacttt
     gtgaatgagt tttacgcata tttgcgtaaa catttctcaa tgatgatact ctctgacgat
     gctgttgtgt gtttcaatag cacttatgca tctcaaggtc tagtggctag cataaagaac
     tttaagtcag ttctttatta tcaaaacaat gtttttatgt ctgaagcaaa atgttggact
     gagactgacc ttactaaagg acctcatgaa ttttgctctc aacatacaat gctagttaaa
     cagggttatg attatgtgta ccttccttac ccagatccat caagaatcct aggggccggc
     tgttttgtag atgatatcgt aaaaacagat ggtacactta tgattgaacg gttcgtgtct
     ttagctatag atgcttaccc acttactaaa catcctaatc aggagtatgc tgatgtcttt
     catttgtact tacaatacat aagaaagcta catgatgagt taacaggaca catgttagac
     atgtattctg ttatgcttac taatgataac acttcaaggt attgggaacc tgagttttat
     gaggctatgt acacaccgca tacagtctta caggctgttg gggcttgtgt tctttgcaat
     tcacagactt cattaagatg tggtgcttgc atacgtagac cattcttatg ttgtaaatgc
     tgttacgacc atgtcatatc aacatcacat aaattagtct tgtctgttaa tccgtatgtt
     tgcaatgctc caggttgtga tgtcacagat gtgactcaac tttacttagg aggtatgagc
     tattattgta aatcacataa accacccatt agttttccat tgtgtgctaa tggacaagtt
     tttggtttat ataaaaatac atgtgttggt agcgataatg ttactgactt taatgcaatt
     gcaacatgtg actggacaaa tgctggtgat tacattttag ctaacacctg tactgaaaga
     ctcaagcttt ttgcagcaga aacgctcaaa gctactgagg agacatttaa actgtcttat
     ggtattgcta ctgtacgtga agtgctgtct gacagagaat tacatctttc atgggaagtt
     ggtaaaccta gaccaccact taaccgaaat tatgtcttta ctggttatcg tgtaactaaa
     aacagtaaag tacaaatagg agagtacacc tttgaaaaag gtgactatgg tgatgctgtt
     gtttaccgag gtacaacaac ttacaaatta aatgttggtg attattttgt gctgacatca
     catacagtaa tgccattaag tgcacctaca ctagtgccac aagagcacta tgttagaatt
     actggcttat acccaacact caatatctca gatgagtttt ctagcaatgt tgcaaattat
     caaaaggttg gtatgcaaaa gtattctaca ctccagggac cacctggtac tggtaagagt
     cattttgcta ttggcctagc tctctactac ccttctgctc gcatagtgta tacagcttgc
     tctcatgccg ctgttgatgc actatgtgag aaggcattaa aatatttgcc tatagataaa
     tgtagtagaa ttatacctgc acgtgctcgt gtagagtgtt ttgataaatt caaagtgaat
     tcaacattag aacagtatgt cttttgtact gtaaatgcat tgcctgagac gacagcagat
     atagttgtct ttgatgaaat ttcaatggcc acaaattatg atttgagtgt tgtcaatgcc
     agattacgtg ctaagcacta tgtgtacatt ggcgaccctg ctcaattacc tgcaccacgc
     acattgctaa ctaagggcac actagaacca gaatatttca attcagtgtg tagacttatg
     aaaactatag gtccagacat gttcctcgga acttgtcggc gttgtcctgc tgaaattgtt
     gacactgtga gtgctttggt ttatgataat aagcttaaag cacataaaga caaatcagct
     caatgcttta aaatgtttta taagggtgtt atcacgcatg atgtttcatc tgcaattaac
     aggccacaaa taggcgtggt aagagaattc cttacacgta accctgcttg gagaaaagct
     gtctttattt caccttataa ttcacagaat gctgtagcct caaagatttt gggactacca
     actcaaactg ttgattcatc acagggctca gaatatgact atgtcatatt cactcaaacc
     actgaaacag ctcactcttg taatgtaaac agatttaatg ttgctattac cagagcaaaa
     gtaggcatac tttgcataat gtctgataga gacctttatg acaagttgca atttacaagt
     cttgaaattc cacgtaggaa tgtggcaact ttacaagctg aaaatgtaac aggactcttt
     aaagattgta gtaaggtaat cactgggtta catcctacac aggcacctac acacctcagt
     gttgacacta aattcaaaac tgaaggttta tgtgttgaca tacctggcat acctaaggac
     atgacctata gaagactcat ctctatgatg ggttttaaaa tgaattatca agttaatggt
     taccctaaca tgtttatcac ccgcgaagaa gctataagac atgtacgtgc atggattggc
     ttcgatgtcg aggggtgtca tgctactaga gaagctgttg gtaccaattt acctttacag
     ctaggttttt ctacaggtgt taacctagtt gctgtaccta caggttatgt tgatacacct
     aataatacag atttttccag agttagtgct aaaccaccgc ctggagatca atttaaacac
     ctcataccac ttatgtacaa aggacttcct tggaatgtag tgcgtataaa gattgtacaa
     atgttaagtg acacacttaa aaatctctct gacagagtcg tatttgtctt atgggcacat
     ggctttgagt tgacatctat gaagtatttt gtgaaaatag gacctgagcg cacctgttgt
     ctatgtgata gacgtgccac atgcttttcc actgcttcag acacttatgc ctgttggcat
     cattctattg gatttgatta cgtctataat ccgtttatga ttgatgttca acaatggggt
     tttacaggta acctacaaag caaccatgat ctgtattgtc aagtccatgg taatgcacat
     gtagctagtt gtgatgcaat catgactagg tgtctagctg tccacgagtg ctttgttaag
     cgtgttgact ggactattga atatcctata attggtgatg aactgaagat taatgcggct
     tgtagaaagg ttcaacacat ggttgttaaa gctgcattat tagcagacaa attcccagtt
     cttcacgaca ttggtaaccc taaagctatt aagtgtgtac ctcaagctga tgtagaatgg
     aagttctatg atgcacagcc ttgtagtgac aaagcttata aaatagaaga attattctat
     tcttatgcca cacattctga caaattcaca gatggtgtat gcctattttg gaattgcaat
     gtcgatagat atcctgctaa ttccattgtt tgtagatttg acactagagt gctatctaac
     cttaacttgc ctggttgtga tggtggcagt ttgtatgtaa ataaacatgc attccacaca
     ccagcttttg ataaaagtgc ttttgttaat ttaaaacaat taccattttt ctattactct
     gacagtccat gtgagtctca tggaaaacaa gtagtgtcag atatagatta tgtaccacta
     aagtctgcta cgtgtataac acgttgcaat ttaggtggtg ctgtctgtag acatcatgct
     aatgagtaca gattgtatct cgatgcttat aacatgatga tctcagctgg ctttagcttg
     tgggtttaca aacaatttga tacttataac ctctggaaca cttttacaag acttcagagt
     ttagaaaatg tggcttttaa tgttgtaaat aagggacact ttgatggaca acagggtgaa
     gtaccagttt ctatcattaa taacactgtt tacacaaaag ttgatggtgt tgatgtagaa
     ttgtttgaaa ataaaacaac attacctgtt aatgtagcat ttgagctttg ggctaagcgc
     aacattaaac cagtaccaga ggtgaaaata ctcaataatt tgggtgtgga cattgctgct
     aatactgtga tctgggacta caaaagagat gctccagcac atatatctac tattggtgtt
     tgttctatga ctgacatagc caagaaacca actgaaacga tttgtgcacc actcactgtc
     ttttttgatg gtagagttga tggtcaagta gacttattta gaaatgcccg taatggtgtt
     cttattacag aaggtagtgt taaaggttta caaccatctg taggtcccaa acaagctagt
     cttaatggag tcacattaat tggagaagcc gtaaaaacac agttcaatta ttataagaaa
     gttgatggtg ttgtccaaca attacctgaa acttacttta ctcagagtag aaatttacaa
     gaatttaaac ccaggagtca aatggaaatt gatttcttag aattagctat ggatgaattc
     attgaacggt ataaattaga aggctatgcc ttcgaacata tcgtttatgg agattttagt
     catagtcagt taggtggttt acatctactg attggactag ctaaacgttt taaggaatca
     ccttttgaat tagaagattt tattcctatg gacagtacag ttaaaaacta tttcataaca
     gatgcgcaaa caggttcatc taagtgtgtg tgttctgtta ttgatttatt acttgatgat
     tttgttgaaa taataaaatc ccaagattta tctgtagttt ctaaggttgt caaagtgact
     attgactata cagaaatttc atttatgctt tggtgtaaag atggccatgt agaaacattt
     tacccaaaat tacaatctag tcaagcgtgg caaccgggtg ttgctatgcc taatctttac
     aaaatgcaaa gaatgctatt agaaaagtgt gaccttcaaa attatggtga tagtgcaaca
     ttacctaaag gcataatgat gaatgtcgca aaatatactc aactgtgtca atatttaaac
     acattaacat tagctgtacc ctataatatg agagttatac attttggtgc tggttctgat
     aaaggagttg caccaggtac agctgtttta agacagtggt tgcctacggg tacgctgctt
     gtcgattcag atcttaatga ctttgtctct gatgcagatt caactttgat tggtgattgt
     gcaactgtac atacagctaa taaatgggat ctcattatta gtgatatgta cgaccctaag
     actaaaaatg ttacaaaaga aaatgactct aaagagggtt ttttcactta catttgtggg
     tttatacaac aaaagctagc tcttggaggt tccgtggcta taaagataac agaacattct
     tggaatgctg atctttataa gctcatggga cacttcgcat ggtggacagc ctttgttact
     aatgtgaatg cgtcatcatc tgaagcattt ttaattggat gtaattatct tggcaaacca
     cgcgaacaaa tagatggtta tgtcatgcat gcaaattaca tattttggag gaatacaaat
     ccaattcagt tgtcttccta ttctttattt gacatgagta aatttcccct taaattaagg
     ggtactgctg ttatgtcttt aaaagaaggt caaatcaatg atatgatttt atctcttctt
     agtaaaggta gacttataat tagagaaaac aacagagttg ttatttctag tgatgttctt
     gttaacaact aaacgaacaa tgtttgtttt tcttgtttta ttgccactag tctctagtca
     gtgtgttaat cttacaacca gaactcaatt accccctgca tacactaatt ctttcacacg
     tggtgtttat taccctgaca aagttttcag atcctcagtt ttacattcaa ctcaggactt
     gttcttacct ttcttttcca atgttacttg gttccatgct atacatgtct ctgggaccaa
     tggtactaag aggtttgata accctgtcct accatttaat gatggtgttt attttgcttc
     cactgagaag tctaacataa taagaggctg gatttttggt actactttag attcgaagac
     ccagtcccta cttattgtta ataacgctac taatgttgtt attaaagtct gtgaatttca
     attttgtaat gatccatttt tgggtgttta ttaccacaaa aacaacaaaa gttggatgga
     aagtgagttc agagtttatt ctagtgcgaa taattgcact tttgaatatg tctctcagcc
     ttttcttatg gaccttgaag gaaaacaggg taatttcaaa aatcttaggg aatttgtgtt
     taagaatatt gatggttatt ttaaaatata ttctaagcac acgcctatta atttagtgcg
     tgatctccct cagggttttt cggctttaga accattggta gatttgccaa taggtattaa
     catcactagg tttcaaactt tacttgcttt acatagaagt tatttgactc ctggtgattc
     ttcttcaggt tggacagctg gtgctgcagc ttattatgtg ggttatcttc aacctaggac
     ttttctatta aaatataatg aaaatggaac cattacagat gctgtagact gtgcacttga
     ccctctctca gaaacaaagt gtacgttgaa atccttcact gtagaaaaag gaatctatca
     aacttctaac tttagagtcc aaccaacaga atctattgtt agatttccta atattacaaa
     cttgtgccct tttggtgaag tttttaacgc caccagattt gcatctgttt atgcttggaa
     caggaagaga atcagcaact gtgttgctga ttattctgtc ctatataatt ccgcatcatt
     ttccactttt aagtgttatg gagtgtctcc tactaaatta aatgatctct gctttactaa
     tgtctatgca gattcatttg taattagagg tgatgaagtc agacaaatcg ctccagggca
     aactggaaag attgctgatt ataattataa attaccagat gattttacag gctgcgttat
     agcttggaat tctaacaatc ttgattctaa ggttggtggt aattataatt acctgtatag
     attgtttagg aagtctaatc tcaaaccttt tgagagagat atttcaactg aaatctatca
     ggccggtagc acaccttgta atggtgttga aggttttaat tgttactttc ctttacaatc
     atatggtttc caacccacta atggtgttgg ttaccaacca tacagagtag tagtactttc
     ttttgaactt ctacatgcac cagcaactgt ttgtggacct aaaaagtcta ctaatttggt
     taaaaacaaa tgtgtcaatt tcaacttcaa tggtttaaca ggcacaggtg ttcttactga
     gtctaacaaa aagtttctgc ctttccaaca atttggcaga gacattgctg acactactga
     tgctgtccgt gatccacaga cacttgagat tcttgacatt acaccatgtt cttttggtgg
     tgtcagtgtt ataacaccag gaacaaatac ttctaaccag gttgctgttc tttatcagga
     tgttaactgc acagaagtcc ctgttgctat tcatgcagat caacttactc ctacttggcg
     tgtttattct acaggttcta atgtttttca aacacgtgca ggctgtttaa taggggctga
     acatgtcaac aactcatatg agtgtgacat acccattggt gcaggtatat gcgctagtta
     tcagactcag actaattctc ctcggcgggc acgtagtgta gctagtcaat ccatcattgc
     ctacactatg tcacttggtg cagaaaattc agttgcttac tctaataact ctattgccat
     acccacaaat tttactatta gtgttaccac agaaattcta ccagtgtcta tgaccaagac
     atcagtagat tgtacaatgt acatttgtgg tgattcaact gaatgcagca atcttttgtt
     gcaatatggc agtttttgta cacaattaaa ccgtgcttta actggaatag ctgttgaaca
     agacaaaaac acccaagaag tttttgcaca agtcaaacaa atttacaaaa caccaccaat
     taaagatttt ggtggtttta atttttcaca aatattacca gatccatcaa aaccaagcaa
     gaggtcattt attgaagatc tacttttcaa caaagtgaca cttgcagatg ctggcttcat
     caaacaatat ggtgattgcc ttggtgatat tgctgctaga gacctcattt gtgcacaaaa
     gtttaacggc cttactgttt tgccaccttt gctcacagat gaaatgattg ctcaatacac
     ttctgcactg ttagcgggta caatcacttc tggttggacc tttggtgcag gtgctgcatt
     acaaatacca tttgctatgc aaatggctta taggtttaat ggtattggag ttacacagaa
     tgttctctat gagaaccaaa aattgattgc caaccaattt aatagtgcta ttggcaaaat
     tcaagactca ctttcttcca cagcaagtgc acttggaaaa cttcaagatg tggtcaacca
     aaatgcacaa gctttaaaca cgcttgttaa acaacttagc tccaattttg gtgcaatttc
     aagtgtttta aatgatatcc tttcacgtct tgacaaagtt gaggctgaag tgcaaattga
     taggttgatc acaggcagac ttcaaagttt gcagacatat gtgactcaac aattaattag
     agctgcagaa atcagagctt ctgctaatct tgctgctact aaaatgtcag agtgtgtact
     tggacaatca aaaagagttg atttttgtgg aaagggctat catcttatgt ccttccctca
     gtcagcacct catggtgtag tcttcttgca tgtgacttat gtccctgcac aagaaaagaa
     cttcacaact gctcctgcca tttgtcatga tggaaaagca cactttcctc gtgaaggtgt
     ctttgtttca aatggcacac actggtttgt aacacaaagg aatttttatg aaccacaaat
     cattactaca gacaacacat ttgtgtctgg taactgtgat gttgtaatag gaattgtcaa
     caacacagtt tatgatcctt tgcaacctga attagactca ttcaaggagg agttagataa
     atattttaag aatcatacat caccagatgt tgatttaggt gacatctctg gcattaatgc
     ttcagttgta aacattcaaa aagaaattga ccgcctcaat gaggttgcca agaatttaaa
     tgaatctctc atcgatctcc aagaacttgg aaagtatgag cagtatataa aatggccatg
     gtacatttgg ctaggtttta tagctggctt gattgccata gtaatggtga caattatgct
     ttgctgtatg accagttgct gtagttgtct caagggctgt tgttcttgtg gatcctgctg
     caaatttgat gaagacgact ctgagccagt gctcaaagga gtcaaattac attacacata
     aacgaactta tggatttgtt tatgagaatc ttcacaattg gaactgtaac tttgaagcaa
     ggtgaaatca aggatgctac tccttcagat tttgttcgcg ctactgcaac gataccgata
     caagcctcac tccctttcgg atggcttatt gttggcgttg cacttcttgc tgtttttcag
     agcgcttcca aaatcataac cctcaaaaag agatggcaac tagcactctc caagggtgtt
     cactttgttt gcaacttgct gttgttgttt gtaacagttt actcacacct tttgctcgtt
     gctgctggcc ttgaagcccc ttttctctat ctttatgctt tagtctactt cttgcagagt
     ataaactttg taagaataat aatgaggctt tggctttgct ggaaatgccg ttccaaaaac
     ccattacttt atgatgccaa ctattttctt tgctggcata ctaattgtta cgactattgt
     ataccttaca atagtgtaac ttcttcaatt gtcattactt caggtgatgg cacaacaagt
     cctatttctg aacatgacta ccagattggt ggttatactg aaaaatggga atctggagta
     aaagactgtg ttgtattaca cagttacttc acttcagact attaccagct gtactcaact
     caattgagta cagacactgg tgttgaacat gttaccttct tcatctacaa taaaattgtt
     gatgagcctg aagaacatgt ccaaattcac acaatcgacg gttcatccgg agttgttaat
     ccagtaatgg aaccaattta tgatgaaccg acgacgacta ctagcgtgcc tttgtaagca
     caagctgatg agtacgaact tatgtactca ttcgtttcgg aagagacagg tacgttaata
     gttaatagcg tacttctttt tcttgctttc gtggtattct tgctagttac actagccatc
     cttactgcgc ttcgattgtg tgcgtactgc tgcaatattg ttaacgtgag tcttgtaaaa
     ccttcttttt acgtttactc tcgtgttaaa aatctgaatt cttctagagt tcctgatctt
     ctggtctaaa cgaactaaat attatattag tttttctgtt tggaacttta attttagcca
     tggcagattc caacggtact attaccgttg aagagcttaa aaagctcctt gaacaatgga
     acctagtaat aggtttccta ttccttacat ggatttgtct tctacaattt gcctatgcca
     acaggaatag gtttttgtat ataattaagt taattttcct ctggctgtta tggccagtaa
     ctttagcttg ttttgtgctt gctgctgttt acagaataaa ttggatcacc ggtggaattg
     ctatcgcaat ggcttgtctt gtaggcttga tgtggctcag ctacttcatt gcttctttca
     gactgtttgc gcgtacgcgt tccatgtggt cattcaatcc agaaactaac attcttctca
     acgtgccact ccatggcact attctgacca gaccgcttct agaaagtgaa ctcgtaatcg
     gagctgtgat ccttcgtgga catcttcgta ttgctggaca ccatctagga cgctgtgaca
     tcaaggacct gcctaaagaa atcactgttg ctacatcacg aacgctttct tattacaaat
     tgggagcttc gcagcgtgta gcaggtgact caggttttgc tgcatacagt cgctacagga
     ttggcaacta taaattaaac acagaccatt ccagtagcag tgacaatatt gctttgcttg
     tacagtaagt gacaacagat gtttcatctc gttgactttc aggttactat agcagagata
     ttactaatta ttatgaggac ttttaaagtt tccatttgga atcttgatta catcataaac
     ctcataatta aaaatttatc taagtcacta actgagaata aatattctca attagatgaa
     gagcaaccaa tggagattga ttaaacgaac atgaaaatta ttcttttctt ggcactgata
     acactcgcta cttgtgagct ttatcactac caagagtgtg ttagaggtac aacagtactt
     ttaaaagaac cttgctcttc tggaacatac gagggcaatt caccatttca tcctctagct
     gataacaaat ttgcactgac ttgctttagc actcaatttg cttttgcttg tcctgacggc
     gtaaaacacg tctatcagtt acgtgccaga tcagtttcac ctaaactgtt catcagacaa
     gaggaagttc aagaacttta ctctccaatt tttcttattg ttgcggcaat agtgtttata
     acactttgct tcacactcaa aagaaagaca gaatgattga actttcatta attgacttct
     atttgtgctt tttagccttt ctgctattcc ttgttttaat tatgcttatt atcttttggt
     tctcacttga actgcaagat cataatgaaa cttgtcacgc ctaaacgaac atgaaatttc
     ttgttttctt aggaatcatc acaactgtag ctgcatttca ccaagaatgt agtttacagt
     catgtactca acatcaacca tatgtagttg atgacccgtg tcctattcac ttctattcta
     aatggtatat tagagtagga gctagaaaat cagcaccttt aattgaattg tgcgtggatg
     aggctggttc taaatcaccc attcagtaca tcgatatcgg taattataca gtttcctgtt
     taccttttac aattaattgc caggaaccta aattgggtag tcttgtagtg cgttgttcgt
     tctatgaaga ctttttagag tatcatgacg ttcgtgttgt tttagatttc atctaaacga
     acaaactaaa atgtctgata atggacccca aaatcagcga aatgcacccc gcattacgtt
     tggtggaccc tcagattcaa ctggcagtaa ccagaatgga gaacgcagtg gggcgcgatc
     aaaacaacgt cggccccaag gtttacccaa taatactgcg tcttggttca ccgctctcac
     tcaacatggc aaggaagacc ttaaattccc tcgaggacaa ggcgttccaa ttaacaccaa
     tagcagtcca gatgaccaaa ttggctacta ccgaagagct accagacgaa ttcgtggtgg
     tgacggtaaa atgaaagatc tcagtccaag atggtatttc tactacctag gaactgggcc
     agaagctgga cttccctatg gtgctaacaa agacggcatc atatgggttg caactgaggg
     agccttgaat acaccaaaag atcacattgg cacccgcaat cctgctaaca atgctgcaat
     cgtgctacaa cttcctcaag gaacaacatt gccaaaaggc ttctacgcag aagggagcag
     aggcggcagt caagcctctt ctcgttcctc atcacgtagt cgcaacagtt caagaaattc
     aactccaggc agcagtaggg gaacttctcc tgctagaatg gctggcaatg gcggtgatgc
     tgctcttgct ttgctgctgc ttgacagatt gaaccagctt gagagcaaaa tgtctggtaa
     aggccaacaa caacaaggcc aaactgtcac taagaaatct gctgctgagg cttctaagaa
     gcctcggcaa aaacgtactg ccactaaagc atacaatgta acacaagctt tcggcagacg
     tggtccagaa caaacccaag gaaattttgg ggaccaggaa ctaatcagac aaggaactga
     ttacaaacat tggccgcaaa ttgcacaatt tgcccccagc gcttcagcgt tcttcggaat
     gtcgcgcatt ggcatggaag tcacaccttc gggaacgtgg ttgacctaca caggtgccat
     caaattggat gacaaagatc caaatttcaa agatcaagtc attttgctga ataagcatat
     tgacgcatac aaaacattcc caccaacaga gcctaaaaag gacaaaaaga agaaggctga
     tgaaactcaa gccttaccgc agagacagaa gaaacagcaa actgtgactc ttcttcctgc
     tgcagatttg gatgatttct ccaaacaatt gcaacaatcc atgagcagtg ctgactcaac
     tcaggcctaa actcatgcag accacacaag gcagatgggc tatataaacg ttttcgcttt
     tccgtttacg atatatagtc tactcttgtg cagaatgaat tctcgtaact acatagcaca
     agtagatgta gttaacttta atctcacata gcaatcttta atcagtgtgt aacattaggg
     aggacttgaa agagccacca cattttcacc gaggccacgc ggagtacgat cgagtgtaca
     gtgaacaatg ctagggagag ctgcctatat ggaagagccc taatgtgtaa aattaatttt
     agtagtgcta tccccatgtg attttaatag cttcttagga gaatgacaaa aaaaaaaaaa
     aaaaaaaaaa aaaaaaaaaa

"""

tsst1 = "".join("".join(tsst1.split("\n")).split(" "))

tsst2 = "".join("".join(tsst2.split("\n")).split(" "))

mat_peptide = "".join("".join(mat_peptide.split("\n")).split(" "))

sars_cov_2 = "".join("".join("".join(sars_cov_2.split("\n")).split(" ")))

print(tsst1)

def find_distance(s, t):
    m = len(s)
    n = len(t)
    d  = [[0 for col in t] for row in s]

    for i in range(0,m):
        d[i][0] = i
    
    for j in range(0, n):
        d[0][j] = j
    
    for j in range (0, n):
        for i in range (0, m):
            if s[i] == t[j]:
                substitutionCost = 0
            else:
                substitutionCost = 1
            
            d[i][j] = min(d[i-1][j] +1,
                          d[i][j-1] +1,
                          d[i-1][j-1] + substitutionCost)
            
            if i > 1 and j > 1 and s[i] == t[i-1] and s[i-1] == t[i]:
                    d[i][j] = min(d[i][j], d[i-2][j-2] + 1)
                
    return d[m-1][n-1]


print("tsst1", len(tsst1))
print("tsst2", len(tsst2))
#print(distance(sars_cov_2, tsst1))
slice_len = len(mat_peptide)
minimum = 100000
min_at = -1
slice_at = ""

for x in range(9000, len(sars_cov_2)-slice_len, 1):
    sars_cov_2_slice = sars_cov_2[x:x+slice_len]
    dist = find_distance(sars_cov_2_slice, mat_peptide)
    print("At slice: ", x, " dist: ", dist, "min: ", minimum)
    if dist < minimum:
        minimum = dist
        min_at = x
        slice_at = sars_cov_2_slice

print("Minimum was found at: ", min_at, "with len: ", minimum, "with slice: ", slice_at)