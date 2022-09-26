public class Especimen extends Organismo {
	private Object _especie;
	private Object _raza;
	private Object _dieta;

	public void getEspecie() {
		return this._especie;
	}

	public void setEspecie(Object aEspecie) {
		this._especie = aEspecie;
	}

	public void getRaza() {
		return this._raza;
	}

	public void setRaza(Object aRaza) {
		this._raza = aRaza;
	}

	public void getDieta() {
		return this._dieta;
	}

	public void setDieta(Object aDieta) {
		this._dieta = aDieta;
	}
}