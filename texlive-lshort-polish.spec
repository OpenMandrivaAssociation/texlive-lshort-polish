%global tl_name lshort-polish
%global tl_revision 63289

Name:		texlive-%{tl_name}
Epoch:		1
Version:	6.4PL1
Release:	%{tl_revision}.1
Summary:	Introduction to LaTeX in Polish
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/lshort/polish
License:	gpl2+
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-polish.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-polish.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is the Polish translation of A Short Introduction to LaTeX2e.

