%define modulename aaMI
%define realver 1.0-1
%define r_library %{_libdir}/R/library

Summary:	Mutual information for protein sequence alignments for R
Name:		R-cran-%{modulename}
Version:	%(echo %realver|tr '-' '.')
Release:	%mkrel 6
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		http://cran.r-project.org/web/packages/%{modulename}/index.html
Source0:	http://cran.r-project.org/src/contrib/%{modulename}_%{realver}.tar.gz
BuildRequires:	R-base
Requires:	R-base
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This package contains five functions. read.FASTA reads in a FASTA-format 
alignment file and parses it into a data frame. read.CX reads in a 
ClustalX .aln-format file and parses it into a data frame. read.Gdoc reads 
in a GeneDoc .msf-format file and parses it into a data frame.The alignment 
data frame returned by each of these functions has the sequence IDs as the 
row names and each site in the alignment is a column in the data frame.The 
program aaMI calculates the mutual information between each pair of sites 
(columns) in the protein sequence alignment data frame.The program aaMIn 
calculates the normalized mutual information between pairs of sites in the 
protein sequence alignment data frame. The normalized mutual information 
of sites i and j is the mutual information of these sites divided by their 
joint entropy.

%prep
%setup -q -c

%build

R CMD build %{modulename}

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/%{r_library}

# (tpg) install
R CMD INSTALL %{modulename} --library=%{buildroot}/%{r_library}

# (tpg) provided by R-base
rm -rf %{buildroot}/%{r_library}/R.css

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{r_library}/%{modulename}
