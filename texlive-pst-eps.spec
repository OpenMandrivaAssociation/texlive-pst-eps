# revision 15878
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-eps
# catalog-date 2007-02-28 00:07:21 +0100
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-pst-eps
Version:	1.0
Release:	1
Summary:	Create EPS files from PSTricks figures
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-eps
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-eps.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-eps.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-eps.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Pst-eps is a PSTricks-based package for exporting PSTricks
images 'on the fly' to encapsulated PostScript (EPS) image
files, which can then be read into a document in the usual way.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/pst-eps/pst-eps.tex
%{_texmfdistdir}/tex/latex/pst-eps/pst-eps.sty
%doc %{_texmfdistdir}/doc/generic/pst-eps/Changes
%doc %{_texmfdistdir}/doc/generic/pst-eps/README
%doc %{_texmfdistdir}/doc/generic/pst-eps/pst-eps-doc.bib
%doc %{_texmfdistdir}/doc/generic/pst-eps/pst-eps-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-eps/pst-eps-doc.tex
%doc %{_texmfdistdir}/doc/generic/pst-eps/spirale.eps
#- source
%doc %{_texmfdistdir}/source/generic/pst-eps/Makefile

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
