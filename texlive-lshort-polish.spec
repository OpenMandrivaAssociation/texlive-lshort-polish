Name:		texlive-lshort-polish
Version:	63289
Release:	2
Summary:	Introduction to LaTeX in Polish
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/lshort/polish
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-polish.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-polish.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
This is the Polish translation of A Short Introduction to
LaTeX2e.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/lshort-polish

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
