# revision 15878
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-eps
# catalog-date 2007-02-28 00:07:21 +0100
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-pst-eps
Version:	1.0
Release:	9
Summary:	Create EPS files from PSTricks figures
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-eps
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-eps.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-eps.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-eps.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Pst-eps is a PSTricks-based package for exporting PSTricks
images 'on the fly' to encapsulated PostScript (EPS) image
files, which can then be read into a document in the usual way.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 755266
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 719345
- texlive-pst-eps
- texlive-pst-eps
- texlive-pst-eps
- texlive-pst-eps

