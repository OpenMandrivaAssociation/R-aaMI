%global packname  aaMI
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          1.0_1
Release:          1
Summary:          Mutual information for protein sequence alignments
Group:            Sciences/Mathematics
License:          GPL version 2 or newer
URL:              http://cran.r-project.org/web/packages/aaMI/index.html
Source0:          http://cran.r-project.org/src/contrib/Archive/aaMI/aaMI_1.0-1.tar.gz
BuildArch:        noarch
Requires:         R-core
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 


%description
This package contains five functions. read.FASTA reads in a FASTA-format
alignment file and parses it into a data frame. read.CX reads in a
ClustalX .aln-format file and parses it into a data frame. read.Gdoc reads
in a GeneDoc .msf-format file and parses it into a data frame. The
alignment data frame returned by each of these functions has the sequence
IDs as the row names and each site in the alignment is a column in the
data frame. The program aaMI calculates the mutual information between
each pair of sites (columns) in the protein sequence alignment data frame.
The program aaMIn calculates the normalized mutual information between
pairs of sites in the protein sequence alignment data frame. The
normalized mutual information of sites i and j is the mutual information
of these sites divided by their joint entropy.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
