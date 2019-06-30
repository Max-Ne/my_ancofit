void split_signal(const char* ifile = ""){
  cout << ifile << endl;

  // open file
  TFile* infile = TFile::Open(ifile);
  TIter next(infile->GetListOfKeys());
  TKey* key;

  // vectors to store parameters / file names
  std:vector<double>p0;
  std:vector<double>p1;
  std:vector<double>p2;
  std:vector<string>sfiles;
  int cc = 1;
  TF1 *obj;

  // read parameters && copy 1st funciton
  while ((key = (TKey*)next())) {
    TClass* cl = gROOT->GetClass(key->GetClassName());
    if (!cl->InheritsFrom("TF1")) continue;
    TF1* f = (TF1*)key->ReadObj();
    if (cc) {
      obj = (TF1*) key->ReadObj(); cc=0;
    }
    p0.push_back(f->GetParameter(0));
    p1.push_back(f->GetParameter(1));
    p2.push_back(f->GetParameter(2));
  }
  infile->Close();

  // create new files: oldname_i.root
  // with scaling for 1 bin each
  string a = ifile;
  a = a.substr(0, a.size()-5) + "_"+"1.root";
  for (int i=0;i<p0.size();i++) {
    stringstream ss;
    ss << i;
    string str = ss.str();
    a = a.substr(0, a.size()-7) + "_"+str+".root";
    cout << a << endl;

    const char* sf = a.c_str();
    TFile* split_file = new TFile(sf,"RECREATE");

    obj->SetParameter(0,p0[i]);
    obj->SetParameter(1,p1[i]);
    obj->SetParameter(2,p2[i]);
    obj->Write();
    split_file->Close();
  }
}
