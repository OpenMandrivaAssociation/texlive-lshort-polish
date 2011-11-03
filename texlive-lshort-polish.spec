# revision 15878
# category Package
# catalog-ctan /info/lshort/polish
# catalog-date 2006-12-28 00:06:45 +0100
# catalog-license pd
# catalog-version undef
Name:		texlive-lshort-polish
Version:	20061228
Release:	1
Summary:	Introduction to LaTeX in Polish
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/lshort/polish
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-polish.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-polish.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This is the Polish translation of A Short Introduction to
LaTeX2e.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/lshort-polish/README
%doc %{_texmfdistdir}/doc/latex/lshort-polish/lshort2e.pdf
%doc %{_texmfdistdir}/doc/latex/lshort-polish/src.zip
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
