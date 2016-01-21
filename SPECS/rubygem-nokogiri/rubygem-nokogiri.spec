%global debug_package %{nil}
%global gemdir %(IFS=: R=($(gem env gempath)); echo ${R[${#R[@]}-1]})
%global gem_name nokogiri

Name: rubygem-nokogiri
Version: 1.6.7.2
Release: 1%{?dist}
Summary: Nokogiri is an HTML, XML, SAX, and Reader parser.
Group: Development/Languages
License: MIT
URL: https://rubygems.org/gems/nokogiri/
Source0: https://rubygems.org/downloads/nokogiri-%{version}-java.gem
%define sha1 nokogiri=c054b456b6227bc007565b35a24c5b97638b3049
BuildRequires: ruby
Requires: ruby
%description
Nokogiri is an HTML, XML, SAX, and Reader parser. Among Nokogiri's many features is the ability to search documents via XPath or CSS3 selectors.
%prep
%setup -q -c -T
%build

%install
gem install -V --local --force --install-dir %{buildroot}/%{gemdir} %{SOURCE0}

%files
%defattr(-,root,root,-)
%{gemdir}

%changelog
* Wed Jan 20 2016 Anish Swaminathan <anishs@vmware.com> 1.6.7.2-1
- Upgrade version.
* Wed Nov 11 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 1.6.6.2-1
- Initial build

